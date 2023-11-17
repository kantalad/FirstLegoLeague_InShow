
#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

from threading import Thread

class MyRobot:

    # Default speed for the robot
    __defaultSpeed__ = 150

    def __init__(self):

        # Calculate the light threshold. Choose values based on your measurements.
        self.black = 9
        self.white = 85
        self.threshold = self.black + 10

        # how much the robot should steer to stay on the line
        self.PROPORTIONAL_GAIN = 4

        # Initialize the sensors.
        self.leftColorSensor = ColorSensor(Port.S1)
        self.gyroSensor = GyroSensor(Port.S2)
        self.touchSensor = TouchSensor(Port.S3)
        self.rightColorSensor = ColorSensor(Port.S4)

        # Initialize the motors.
        self.leftMotor = Motor(Port.A)
        self.frontMotor = Motor(Port.B)
        #self.backMotor = Motor(Port.C)
        self.rightMotor = Motor(Port.D)
    
        # Whether the robot is driving
        self.isDriving = False

        # Initialize the drive base.
        self.driveBase = DriveBase(left_motor=self.leftMotor, right_motor=self.rightMotor, wheel_diameter=100.00, axle_track=90)
        self.driveBase.settings(straight_speed=self.__defaultSpeed__, straight_acceleration=self.__defaultSpeed__, turn_rate=self.__defaultSpeed__, turn_acceleration=self.__defaultSpeed__)


    def driveUntilBump(self, speed=__defaultSpeed__):
        t1 = Thread(target=self.__driveUntilBumpThread, args=(speed,))
        t1.start()
        wait(10)

    def __driveUntilBumpThread(self, speed=__defaultSpeed__):
        self.isDriving = True
        self.driveBase.reset()
        self.gyroSensor.reset_angle(angle=0)
        print(self.gyroSensor.angle())
        while not self.touchSensor.pressed():
            print(self.gyroSensor.angle())
            correction = 3 * self.gyroSensor.angle() * -1
            self.driveBase.drive(speed=speed, turn_rate=correction)
        self.driveBase.stop()
        self.isDriving = False
        print(self.gyroSensor.angle())


    def drive(self, distance=0, speed=__defaultSpeed__):
         t1 = Thread(target=self.__driveThread, args=(distance, speed))
         t1.start()
         wait(10)

    def driveBackwards(self, distance=0, speed=__defaultSpeed__):
         t1 = Thread(target=self.__driveThread, args=(distance, (-1*speed)))
         t1.start()
         wait(10)


    def __driveThread(self, distance=0, speed=__defaultSpeed__):
        self.isDriving = True
        self.driveBase.reset()
        self.gyroSensor.reset_angle(angle=0)
        while abs(self.driveBase.distance()) <= distance:
            print(self.gyroSensor.angle())
            correction = 3 * self.gyroSensor.angle() * -1
            self.driveBase.drive(speed=speed, turn_rate=correction)
        self.driveBase.stop()
        self.isDriving = False
        print(self.gyroSensor.angle())


    def turn(self, angle=0, gyro=True):
        t1 = Thread(target=self.__turnThread, args=(0, angle, gyro))
        t1.start()
        wait(10)

    def __turnThread(self, speed=0, angle=0, gyro=True):
        self.isDriving = True
        self.driveBase.reset()
        self.gyroSensor.reset_angle(angle=0)
        print(self.gyroSensor.angle())

        if gyro:
            while self.gyroSensor.angle() != angle:
                print(self.gyroSensor.angle())
                correction = 3*(angle - self.gyroSensor.angle())
                self.driveBase.drive(speed=speed, turn_rate=(correction))
            self.driveBase.stop()

        else:        
            self.driveBase.turn(angle=angle)
            self.driveBase.stop()
        
        self.isDriving = False
        print(self.gyroSensor.angle())


    def followLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__followLine, args=(speed,))
         t1.start()
         wait(10)

    def __followLine(self, speed=__defaultSpeed__):
        self.isDriving = True
        self.driveBase.reset()

        while True:
            deviation = 0
            lReflection = self.leftColorSensor.reflection()
            rReflection = self.rightColorSensor.reflection()
            print("threshold, ", self.threshold, " lReflection: ", lReflection, " rReflection: ", rReflection)

            # If both found black, stop
            if(lReflection <= self.threshold) and (rReflection <= self.threshold):
                print("both found black")
                break

            # If both found white, keep going
            if(self.threshold < lReflection) and (self.threshold < rReflection):
                print("both found white, go straight")
                self.driveBase.drive(speed=speed, turn_rate=0)

            # if left on black, turn left a little
            if lReflection <= self.threshold:
                deviation = lReflection - self.threshold
                correction = self.PROPORTIONAL_GAIN * deviation
                print("left on black, turn left a little. deviation: ", deviation, " correction: ", correction)
                self.driveBase.drive(speed=speed, turn_rate=correction)

            # if left on black, turn right a little
            if rReflection <= self.threshold:
                deviation = rReflection - self.threshold
                correction = self.PROPORTIONAL_GAIN * deviation * -1
                print("right on black, turn right a little. deviation:", deviation, " correction: ", correction)
                self.driveBase.drive(speed=speed, turn_rate=correction)

        self.driveBase.stop()
        self.isDriving = False


    def findLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__findLine, args=(speed, ))
         t1.start()
         wait(10)

    def __findLine(self, speed=__defaultSpeed__):
        self.isDriving = True
        self.driveBase.reset()
        self.gyroSensor.reset_angle(angle=0)

        while True:
            lReflection = self.leftColorSensor.reflection()
            rReflection = self.rightColorSensor.reflection()
            print("threshold, ", self.threshold, " lReflection: ", lReflection, " rReflection: ", rReflection)

            # If both found white, keep going
            if(lReflection <= self.threshold) or (rReflection <= self.threshold):
                print("someone found black, stop")
                break

            print("both found white, go straight")
            correction = 3 * self.gyroSensor.angle() * -1
            self.driveBase.drive(speed=speed, turn_rate=correction)

        self.driveBase.stop()
        self.isDriving = False

    def frontUntilTarget(self, speed=__defaultSpeed__, target_angle=0, then=Stop.HOLD, wait=False):
        self.frontMotor.run_target(speed=speed, target_angle=target_angle, then=then, wait=wait)

    def frontUntilStalled(self, speed=__defaultSpeed__, then=Stop.HOLD, duty_limit=None):
        self.frontMotor.run_until_stalled(speed=speed, then=then, duty_limit=duty_limit)


    def frontStop(self):
        self.frontMotor.stop()

    """
    def backUntilStalled(self, speed=500, target_angle=0, then=Stop.HOLD):
        self.backMotor.run_target(speed=speed, target_angle=target_angle, then=then, wait=False)

    def backStop(self):
        self.backMotor.stop()
    """

    def wait(self, time=1000):
        wait(time)

    def waitUntilFinishedDriving(self):
        while self.isDriving:
            wait(10)

