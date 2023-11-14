#!/usr/bin/env pybricks-micropython

class M08_RollingCamera:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def name(self):
        return "M08: Rolling Camera"

    def go(self):
        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

