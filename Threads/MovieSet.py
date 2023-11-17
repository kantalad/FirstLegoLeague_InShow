#!/usr/bin/env pybricks-micropython

from Missions.M09_MovieSet import M09_MovieSet
from Modules.MenuItem import MenuItem

class MovieSet(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m09 = M09_MovieSet(myRobot=myRobot)

    def __go(self):
        self.m09.go()
