
#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Stop
from pybricks.tools import wait
from threading import Thread

class MyRobot:

    # Default speed for the robot
    __defaultSpeed__ = 150

    def __init__(self):
        # Whether the robot is driving
        self.isDriving = False

    def driveUntilBump(self, speed=__defaultSpeed__):
        t1 = Thread(target=self.__driveUntilBumpThread, args=(speed,))
        t1.start()
        wait(10)

    def __driveUntilBumpThread(self, speed=__defaultSpeed__):
        self.isDriving = True
        print("drive unitl bump started")
        wait(2000)
        print("drive unitl bump finished")
        self.isDriving = False


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
        print("drive started, speed: ", speed)
        wait(distance*10)
        print("drive finished, speed:", speed)
        self.isDriving = False


    def turn(self, angle=0, gyro=True):
        t1 = Thread(target=self.__turnThread, args=(0, angle, gyro))
        t1.start()
        wait(10)

    def __turnThread(self, speed=0, angle=0, gyro=True):
        self.isDriving = True
        print("turn started")
        wait(angle*10)
        print("turn finished")
        self.isDriving = False


    def followLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__followLine, args=(speed,))
         t1.start()
         wait(10)

    def __followLine(self, speed=__defaultSpeed__):
        self.isDriving = True
        print("follow line started")
        wait(2000)
        print("follow line ended")
        self.isDriving = False


    def findLine(self, speed=__defaultSpeed__):
         t1 = Thread(target=self.__findLine, args=(speed, ))
         t1.start()
         wait(10)

    def __findLine(self, speed=__defaultSpeed__):
        self.isDriving = True
        print("find line started")
        wait(2000)
        print("fine line finished")
        self.isDriving = False


    def frontUntilTarget(self, speed=__defaultSpeed__, target_angle=0, then=Stop.HOLD, wait=False):
        print("front motor until target started")
        if wait:
            self.wait(target_angle*10)
        print("front motor until target finished")

    def frontUntilStalled(self, speed=__defaultSpeed__, then=Stop.HOLD, duty_limit=None):
        print("front motor until stalled started")
        wait(1000)
        print("front motor until stalled finished")

    def frontStop(self):
        print("front motor stopped")


    def backUntilTarget(self, speed=__defaultSpeed__, target_angle=0, then=Stop.HOLD, wait=False):
        print("back motor untii target started")
        if wait :
            self.wait(target_angle*10)
        print("back motor until target finished")

    def backUntilStalled(self, speed=500, target_angle=0, then=Stop.HOLD):
        print("back motor until stalled started")
        wait(1000)
        print("back motor until stalled finished")

    def backStop(self):
        print("back motor stopped")


    def wait(self, time=1000):
        print("Wait started")
        wait(time)
        print("wait finished")

    def waitUntilFinishedDriving(self):
        print("waiting until finished driving started")
        while self.isDriving:
            wait(10)
        print("waiting until finished driving finished")
