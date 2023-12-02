#!/usr/bin/env pybricks-micropython

from Missions.M09_MovieSet import M09_MovieSet
from Modules.MenuItem import MenuItem

class MovieSet(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m09 = M09_MovieSet(myRobot=myRobot)

    def __go(self):

        self.myRobot.frontUntilStalled(speed=-360, duty_limit=30)

        self.myRobot.turn(angle=90)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.m09.go()

        self.myRobot.frontStop()

        self.myRobot.driveBackwards(speed=250, distance=400)
        self.myRobot.waitUntilFinishedDriving()        
