#!/usr/bin/env pybricks-micropython

class M09_MovieSet:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def go(self):
        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

