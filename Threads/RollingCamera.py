#!/usr/bin/env pybricks-micropython

from Missions.M08_RollingCamera import M08_RollingCamera
from Modules.MenuItem import MenuItem

class RollingCamera(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m08 = M08_RollingCamera(myRobot=myRobot)

    def __go(self):
        self.m08.go()

