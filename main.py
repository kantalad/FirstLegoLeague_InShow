#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick

from Modules.MyRobot import MyRobot
#from Modules.MyMockRobot import MyRobot
from Modules.MenuSystem import MenuSystem

from Threads.MovieSet import MovieSet
from Threads.SoundMixer import SoundMixer
from Threads.Dragon import Dragon
from Threads.BigRun import BigRun
from Threads.RollingCamera import RollingCamera 
from Threads.CraftTableFront import CraftTableFront
from Threads.LightShow import LightShow
from Missions.ME_GoUntilBump import ME_GoUntilBump
from Missions.ME_GoUntilBumpComeBack import ME_GoUntilBumpComeBack
from Missions.ME_Drive import ME_Drive
from Missions.ME_DriveComeBack import ME_DriveComeBack

from Missions.TESTING import TESTING


# Initialze brick
ev3 = EV3Brick()

# Initialize robot
myRobot = MyRobot()

# Initialize and start menu system
menuSystem = MenuSystem(ev3=ev3)
menuSystem.addItem(TESTING(myRobot))
menuSystem.addItem(MovieSet(myRobot))
menuSystem.addItem(SoundMixer(myRobot))
menuSystem.addItem(Dragon(myRobot))
menuSystem.addItem(BigRun(myRobot))
menuSystem.addItem(RollingCamera(myRobot))
menuSystem.addItem(CraftTableFront(myRobot))
menuSystem.addItem(LightShow(myRobot))
menuSystem.addItem(ME_GoUntilBump(myRobot))
menuSystem.addItem(ME_GoUntilBumpComeBack(myRobot))
menuSystem.addItem(ME_Drive(myRobot))
menuSystem.addItem(ME_DriveComeBack(myRobot))
menuSystem.go()
