#!/usr/bin/env pybricks-micropython

from Missions.M02_TheaterSceneChange import M02_TheaterSceneChange
from Missions.M03_ImmersiveExperience import M03_ImmersiveExperience
from Missions.M04_Masterpiece import M04_Masterpiece
from Missions.M05_AugmentedReality import M05_AugmentedReality
from Modules.MenuItem import MenuItem

class BigRun(MenuItem):

    def __init__(self, myRobot):
        super().__init__(myRobot=myRobot)
        self.m02 = M02_TheaterSceneChange(myRobot=myRobot)
        self.m03 = M03_ImmersiveExperience(myRobot=myRobot)
        self.m04 = M04_Masterpiece(myRobot=myRobot)
        self.m05 = M05_AugmentedReality(myRobot=myRobot)

    def __go(self):
        self.m02.go()
        self.m03.go()
        self.m04.go()
        self.m05.go()

        # M13 Back of craft table
        # M07 Hologram
        # M06 left side Music Concert LS

