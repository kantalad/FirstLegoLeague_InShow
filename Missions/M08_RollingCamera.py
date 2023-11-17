#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M08_RollingCamera(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.frontUntilStalled(speed=360)
        self.myRobot.frontUntilStalled(speed=-360)

        self.myRobot.driveBackwards(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.turn(angle=-45)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.drive(distance=100)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveBackwards(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()
