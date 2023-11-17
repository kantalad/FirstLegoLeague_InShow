#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M01_Dragon(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.turn(angle=90, gyro=False)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveBackwards(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()
