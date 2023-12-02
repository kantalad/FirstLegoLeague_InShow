#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Color

from Modules.MenuItem import MenuItem

class TESTING(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)

    def __go(self):
        

        #frontUntilTarget(self, speed=__defaultSpeed__, target_angle=0, then=Stop.HOLD, wait=False)

        #self.myRobot.frontUntilStalled(speed=-100)
        #self.myRobot.frontUntilStalled(speed=100)

        self.myRobot.turn(angle=90)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.driveUntilBump()
        self.myRobot.waitUntilFinishedDriving()



        """
        self.myRobot.findLine(color=Color.BLACK)
        self.myRobot.waitUntilFinishedDriving()
        """

        """
        self.myRobot.turn(angle=-15)
        self.myRobot.waitUntilFinishedDriving()
        
        self.myRobot.drive(distance=15)
        self.myRobot.waitUntilFinishedDriving()

        self.myRobot.followLine()
        self.myRobot.waitUntilFinishedDriving()
        """
