#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M01_Dragon(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        #self.myRobot.frontUntilStalled(speed=360, duty_limit=30)
        self.myRobot.frontUntilTarget(speed=50, target_angle=0)

        self.myRobot.driveBackwards(speed=100, distance=40)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.turn(angle=100, gyro=False)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveBackwards(speed=100, distance=10)
        self.myRobot.waitUntilFinishedDriving()
