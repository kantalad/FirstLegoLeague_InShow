#!/usr/bin/env pybricks-micropython

class M02_TheaterSceneChange:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def name(self):
        return "M02: Theater Scene Change"

    def go(self):
        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

