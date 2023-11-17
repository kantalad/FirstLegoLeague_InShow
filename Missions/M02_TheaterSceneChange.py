#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M02_TheaterSceneChange(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):
        
        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        for x in range(1, 3):
            self.myRobot.frontUntilStalled(speed=-360)
            self.myRobot.frontUntilTarget(target_angle=0, wait=True)

        self.myRobot.driveBackwards(speed=100, distance=100)
        self.myRobot.waitUntilFinishedDriving()


