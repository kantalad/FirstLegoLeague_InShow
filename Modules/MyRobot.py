
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

    # Calculate the light threshold. Choose values based on your measurements.
    __BLACK = 9
    __WHITE = 85
    #__threshold = (__BLACK + __WHITE) / 2
    __threshold = __BLACK + 10

    # how much the robot should steer to stay on the line
    __PROPORTIONAL_GAIN = 4

    # Initialize the sensors.
    __leftColorSensor = ColorSensor(Port.S1)
    __gyroSensor = GyroSensor(Port.S2)
    __touchSensor = TouchSensor(Port.S3)
    __rightColorSensor = ColorSensor(Port.S4)

    # Initialize the motors.
    __leftMotor = Motor(Port.A)
    __frontMotor = Motor(Port.B)
    #__backMotor = Motor(Port.C)
    __rightMotor = Motor(Port.D)
 
    # Whether the robot is driving
    __IsDriving = False

    # Initialize the drive base.
    __driveBase = DriveBase(left_motor=__leftMotor, right_motor=__rightMotor, wheel_diameter=100.00, axle_track=90)

    def __init__(self):
        self.__driveBase.settings(straight_speed=self.__defaultSpeed__, straight_acceleration=self.__defaultSpeed__, turn_rate=0, turn_acceleration=self.__defaultSpeed__)
        #self.recalibrateGyro()

    def driveUntilBump(self, speed=__defaultSpeed__):
        t1 = Thread(target=self.__driveUntilBumpThread, args=(speed,))
        t1.start()
        wait(10)

    def __driveUntilBumpThread(self, speed=__defaultSpeed__):
        self.__IsDriving = True
        self.__driveBase.reset()
        self.__gyroSensor.reset_angle(angle=0)
        print(self.__gyroSensor.angle())
        while not self.__touchSensor.pressed():
            print(self.__gyroSensor.angle())
            correction = 3 * self.__gyroSensor.angle() * -1
            self.__driveBase.drive(speed=speed, turn_rate=correction)
        self.__driveBase.stop()
        self.__IsDriving = False
        print(self.__gyroSensor.angle())


    def drive(self, distance=0, speed=__defaultSpeed__):
         t1 = Thread(target=self.__driveThread, args=(distance, speed))
         t1.start()
         wait(10)

    def driveBackwards(self, distance=0, speed=__defaultSpeed__):
         t1 = Thread(target=self.__driveThread, args=(distance, (-1*speed)))
         t1.start()
         wait(10)


    def __driveThread(self, distance=0, speed=__defaultSpeed__):
        self.__IsDriving = True
        self.__driveBase.reset()
        self.__gyroSensor.reset_angle(angle=0)
        while abs(self.__driveBase.distance()) <= distance:
            print(self.__gyroSensor.angle())
            correction = 3 * self.__gyroSensor.angle() * -1
            self.__driveBase.drive(speed=speed, turn_rate=correction)
        self.__driveBase.stop()
        self.__IsDriving = False
        print(self.__gyroSensor.angle())


    def turn(self, angle=0):
        t1 = Thread(target=self.__turnThread, args=(0, angle))
        t1.start()
        wait(10)

    def __turnThread(self, speed=0, angle=0):
        self.__IsDriving = True
        self.__driveBase.reset()
        self.__gyroSensor.reset_angle(angle=0)
        print(self.__gyroSensor.angle())
        while self.__gyroSensor.angle() != angle:
            print(self.__gyroSensor.angle())
            correction = 3*(angle - self.__gyroSensor.angle())
            self.__driveBase.drive(speed=speed, turn_rate=(correction))
        self.__driveBase.stop()
        self.__IsDriving = False
        print(self.__gyroSensor.angle())


    def followLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__followLine, args=(speed,))
         t1.start()
         wait(10)

    def __followLine(self, speed=__defaultSpeed__):
        self.__IsDriving = True
        self.__driveBase.reset()

        while True:
            deviation = 0
            lReflection = self.__leftColorSensor.reflection()
            rReflection = self.__rightColorSensor.reflection()
            print("threshold, ", self.__threshold, " lReflection: ", lReflection, " rReflection: ", rReflection)

            # If both found black, stop
            if(lReflection <= self.__threshold) and (rReflection <= self.__threshold):
                print("both found black")
                break

            # If both found white, keep going
            if(self.__threshold < lReflection) and (self.__threshold < rReflection):
                print("both found white, go straight")
                self.__driveBase.drive(speed=speed, turn_rate=0)

            # if left on black, turn left a little
            if lReflection <= self.__threshold:
                deviation = lReflection - self.__threshold
                correction = self.__PROPORTIONAL_GAIN * deviation
                print("left on black, turn left a little. deviation: ", deviation, " correction: ", correction)
                self.__driveBase.drive(speed=speed, turn_rate=correction)

            # if left on black, turn right a little
            if rReflection <= self.__threshold:
                deviation = rReflection - self.__threshold
                correction = self.__PROPORTIONAL_GAIN * deviation * -1
                print("right on black, turn right a little. deviation:", deviation, " correction: ", correction)
                self.__driveBase.drive(speed=speed, turn_rate=correction)

        self.__driveBase.stop()
        self.__IsDriving = False


    def findLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__findLine, args=(speed, ))
         t1.start()
         wait(10)

    def __findLine(self, speed=__defaultSpeed__):
        self.__IsDriving = True
        self.__driveBase.reset()
        self.__gyroSensor.reset_angle(angle=0)

        while True:
            lReflection = self.__leftColorSensor.reflection()
            rReflection = self.__rightColorSensor.reflection()
            print("threshold, ", self.__threshold, " lReflection: ", lReflection, " rReflection: ", rReflection)

            # If both found white, keep going
            if(lReflection <= self.__threshold) or (rReflection <= self.__threshold):
                print("someone found black, stop")
                break

            print("both found white, go straight")
            correction = 3 * self.__gyroSensor.angle() * -1
            self.__driveBase.drive(speed=speed, turn_rate=correction)

        self.__driveBase.stop()
        self.__IsDriving = False

    """
    def __findLine(self, speed=__defaultSpeed__):
        self.__IsDriving = True
        self.__driveBase.reset()
        self.__gyroSensor.reset_angle(angle=0)

        while True:
            lReflection = self.__leftColorSensor.reflection()
            rReflection = self.__rightColorSensor.reflection()
            print("threshold, ", self.__threshold, " lReflection: ", lReflection, " rReflection: ", rReflection)

            # If both found white, keep going
            if(lReflection < self.__threshold) or (rReflection < self.__threshold):
                print("someone found black, stop")
                break

            print("both found white, go straight")
            correction = 3 * self.__gyroSensor.angle() * -1
            self.__driveBase.drive(speed=speed, turn_rate=correction)

        self.__driveBase.stop()
        self.__IsDriving = False
    """

    def frontUntilTarget(self, speed=__defaultSpeed__, target_angle=0, then=Stop.HOLD, wait=False):
        self.__frontMotor.run_target(speed=speed, target_angle=target_angle, then=then, wait=wait)

    def frontUntilStalled(self, speed=__defaultSpeed__, then=Stop.HOLD, duty_limit=None):
        self.__frontMotor.run_until_stalled(speed=speed, then=then, duty_limit=duty_limit)


    def frontStop(self):
        self.__frontMotor.stop()

    """
    def backUntilStalled(self, speed=500, target_angle=0, then=Stop.HOLD):
        self.__backMotor.run_target(speed=speed, target_angle=target_angle, then=then, wait=False)

    def backStop(self):
        self.__backMotor.stop()
    """

    """
    # This does not work
    def recalibrateGyro(self):
        print("recalibrateGyro - start")
        self.__gyroSensor.angle()
        self.__gyroSensor.speed()
        self.__gyroSensor.angle()
        wait(250)
        print("recalibrateGyro - done")
    """

    def wait(self, time=1000):
        wait(time)

    def waitUntilFinishedDriving(self):
        while self.__IsDriving:
            wait(10)

