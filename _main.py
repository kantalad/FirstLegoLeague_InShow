#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick

#from Modules.MyRobot import MyRobot
from Modules.MyMockRobot import MyRobot
from Modules.MenuSystem import MenuSystem

from Missions.M01_Dragon import M01_Dragon
from Missions.M02_TheaterSceneChange import M02_TheaterSceneChange
from Missions.M03_ImmersiveExperience import M03_ImmersiveExperience
from Missions.M04_Masterpiece import M04_Masterpiece
from Missions.M05_AugmentedReality import M05_AugmentedReality
from Missions.M06_MusicConcertLS import M06_MusicConcertLS
from Missions.M07_Hologram import M07_Hologram
from Missions.M08_RollingCamera import M08_RollingCamera
from Missions.M09_MovieSet import M09_MovieSet
from Missions.M10_SoundMixer import M10_SoundMixer
from Missions.M11_LightShow import M11_LightShow
from Missions.M12_VRArtist import M12_VRArtist
from Missions.M13_CraftCreator import M13_CraftCreator
from Missions.M14_AudienceDelivery import M14_AudienceDelivery
from Missions.M15_ExpertDelivery import M15_ExpertDelivery


# Initialze brick
ev3 = EV3Brick()

# Initialize robot
myRobot = MyRobot()

# Initialize and start menu system
menuSystem = MenuSystem(ev3=ev3, myRobot=myRobot)
menuSystem.addItem(M01_Dragon(myRobot))
menuSystem.addItem(M02_TheaterSceneChange(myRobot))
menuSystem.addItem(M03_ImmersiveExperience(myRobot))
menuSystem.addItem(M04_Masterpiece(myRobot))
menuSystem.addItem(M05_AugmentedReality(myRobot))
"""
menuSystem.addItem(M06_MusicConcertLS(myRobot))
menuSystem.addItem(M07_Hologram(myRobot))
menuSystem.addItem(M08_RollingCamera(myRobot))
menuSystem.addItem(M09_MovieSet(myRobot))
menuSystem.addItem(M10_SoundMixer(myRobot))
menuSystem.addItem(M11_LightShow(myRobot))
menuSystem.addItem(M12_VRArtist(myRobot))
menuSystem.addItem(M13_CraftCreator(myRobot))
menuSystem.addItem(M14_AudienceDelivery(myRobot))
menuSystem.addItem(M15_ExpertDelivery(myRobot))
"""
menuSystem.start()


#from Missions.M01_Dragon import M01_Dragon
#from Missions.M04_Masterpiece import M04_Masterpiece

#m01 = M01_Dragon(myRobot)
#m01.go()

#m04 = M04_Masterpiece(myRobot)
#m04.go()
