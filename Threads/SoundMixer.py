#!/usr/bin/env pybricks-micropython

from Missions.M10_SoundMixer import M10_SoundMixer
from Modules.MenuItem import MenuItem

class SoundMixer(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m10 = M10_SoundMixer(myRobot=myRobot)

    def __go(self):

        self.myRobot.frontUntilStalled(speed=-360, duty_limit=30)

        self.myRobot.turn(angle=45)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()

        self.m10.go()

        self.myRobot.frontStop()

        self.myRobot.driveBackwards(speed=250, distance=400)
        self.myRobot.waitUntilFinishedDriving()

