#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M11_LightShow(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()
