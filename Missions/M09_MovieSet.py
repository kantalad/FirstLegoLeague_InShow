#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M09_MovieSet(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        # Robot should be parallel with track near wall

        # Micro turn to get loop
        self.myRobot.turn(angle=-45)
        self.myRobot.waitUntilFinishedDriving()

        # Get the loop
        self.myRobot.frontUntilStalled(speed=360, duty_limit=30)

        # Move loop to position
        self.myRobot.turn(angle=-60)
        self.myRobot.waitUntilFinishedDriving()

        # lift front
        self.myRobot.frontUntilStalled(speed=-360, duty_limit=30)

        # turn towards latch
        self.myRobot.turn(angle=90)
        self.myRobot.waitUntilFinishedDriving()

        # push down latch
        self.myRobot.frontUntilStalled(speed=360, duty_limit=30)

