#!/usr/bin/env pybricks-micropython

class M11_LightShow:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def name(self):
        return "M11: Light Show"

    def go(self):
        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

