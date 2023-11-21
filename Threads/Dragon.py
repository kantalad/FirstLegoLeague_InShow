#!/usr/bin/env pybricks-micropython

from Missions.M01_Dragon import M01_Dragon
from Modules.MenuItem import MenuItem

class Dragon(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m01 = M01_Dragon(myRobot=myRobot)

    def __go(self):

        self.myRobot.drive(distance=15)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.turn(angle=-15)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.m01.go()

        self.myRobot.driveBackwards(speed=250, distance=400)
        self.myRobot.waitUntilFinishedDriving()


