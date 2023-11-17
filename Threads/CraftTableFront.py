#!/usr/bin/env pybricks-micropython

from Missions.M13_CraftCreator import M13_CraftCreator
from Modules.MenuItem import MenuItem

class CraftTableFront(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m13 = M13_CraftCreator(myRobot=myRobot)

    def __go(self):
        self.m13.go()

