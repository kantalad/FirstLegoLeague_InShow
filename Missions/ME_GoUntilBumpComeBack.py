#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class ME_GoUntilBumpComeBack(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):
        
        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveBackwards(distance=1000)
        self.myRobot.waitUntilFinishedDriving()
