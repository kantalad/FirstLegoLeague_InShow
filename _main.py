#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick

#from Modules.MyRobot import MyRobot
from Modules.MyMockRobot import MyRobot
from Modules.MenuSystem import MenuSystem


# Initialze brick
ev3 = EV3Brick()

# Initialize robot
myRobot = MyRobot()

# Initialize and start menu system
menuSystem = MenuSystem(ev3=ev3, myRobot=myRobot)
menuSystem.start()



#from Missions.M01_Dragon import M01_Dragon
#from Missions.M04_Masterpiece import M04_Masterpiece

#m01 = M01_Dragon(myRobot)
#m01.go()

#m04 = M04_Masterpiece(myRobot)
#m04.go()
