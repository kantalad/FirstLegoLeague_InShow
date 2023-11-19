#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class TESTING(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):
        

        self.myRobot.findLine()
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.turn(angle=-15)
        self.myRobot.waitUntilFinishedDriving()
        
        self.myRobot.drive(distance=15)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.followLine()
        self.myRobot.waitUntilFinishedDriving()

