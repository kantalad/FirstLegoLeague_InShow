#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M10_SoundMixer(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        # back up a little, you are bumping the model at this point
        self.myRobot.driveBackwards(distance=50, speed=50)
        self.myRobot.waitUntilFinishedDriving()

        # bring the attachment down
        self.myRobot.frontUntilStalled(speed=360, duty_limit=30)

        # Start moving attachment up and drive forward at same time
        self.myRobot.frontUntilTarget(speed=50, target_angle=-15)
        #self.myRobot.frontUntilStalled(speed=-50, duty_limit=30)
        self.myRobot.drive(distance=10, speed=50)
        self.myRobot.waitUntilFinishedDriving()

        # We may need to wait for the front to finish going up
        #self.myRobot.wait(time=5000)

        # turn the right a little to hold up the middle
        self.myRobot.turn(angle=30)
        self.myRobot.waitUntilFinishedDriving()

        # This holds up the middle while letting the sides fall
        self.myRobot.wait(time=1000)