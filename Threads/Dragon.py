#!/usr/bin/env pybricks-micropython

from Missions.M01_Dragon import M01_Dragon
from Modules.MenuItem import MenuItem

class Dragon(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m01 = M01_Dragon(myRobot=myRobot)

    def __go(self):
        self.m01.go()
