#!/usr/bin/env pybricks-micropython

from Modules.MenuItem import MenuItem

class M09_MovieSet(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):

        # Robot should be parallel with track near wall

        self.myRobot.driveBackwards(speed=50, distance=45)
        self.myRobot.waitUntilFinishedDriving()        

        # Micro turn to get loop
        #self.myRobot.turn(angle=-15)
        #self.myRobot.waitUntilFinishedDriving()

        # Get the loop
        self.myRobot.frontUntilStalled(speed=360, duty_limit=30)
        #self.myRobot.wait(time=2000)

        self.myRobot.driveBackwards(speed=50, distance=100)
        self.myRobot.waitUntilFinishedDriving()        

        self.myRobot.turn(angle=-30)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.drive(speed=50, distance=50)
        self.myRobot.waitUntilFinishedDriving()        

        # lift front
        self.myRobot.frontUntilStalled(speed=-360, duty_limit=30)


        """
        self.myRobot.drive(speed=50, distance=20)
        self.myRobot.waitUntilFinishedDriving()        

        # Move loop to position
        self.myRobot.turn(angle=-20)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.drive(speed=50, distance=20)
        self.myRobot.waitUntilFinishedDriving()        

        # Move loop to position
        self.myRobot.turn(angle=-25)
        self.myRobot.waitUntilFinishedDriving()

        # lift front
        self.myRobot.frontUntilStalled(speed=-360, duty_limit=30)

        # turn towards latch
        self.myRobot.turn(angle=90)
        self.myRobot.waitUntilFinishedDriving()

        # push down latch
        self.myRobot.frontUntilStalled(speed=360, duty_limit=30)
        """
