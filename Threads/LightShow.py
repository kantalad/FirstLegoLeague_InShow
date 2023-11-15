#!/usr/bin/env pybricks-micropython

from Missions.M11_LightShow import M11_LightShow
from Modules.MenuItem import MenuItem

class LightShow(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m11 = M11_LightShow(myRobot=myRobot)

    def __go(self):
        self.m11.go()

