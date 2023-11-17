#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M04_Masterpiece(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        self.myRobot.drive(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.frontUntilStalled(speed=-360)
        self.myRobot.frontUntilTarget(target_angle=0, wait=True)

        self.myRobot.driveBackwards(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()
