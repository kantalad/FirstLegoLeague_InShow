#!/usr/bin/env pybricks-micropython

from Missions.M10_SoundMixer import M10_SoundMixer
from Modules.MenuItem import MenuItem

class SoundMixer(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m10 = M10_SoundMixer(myRobot=myRobot)

    def __go(self):
        self.m10.go()
