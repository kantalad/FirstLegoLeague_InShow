#!/usr/bin/env pybricks-micropython

class M01_Dragon:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def go(self):

        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

        self.__myRobot.turn(angle=90)
        self.__myRobot.waitUntilFinishedDriving()

        self.__myRobot.driveBackwards(speed=100, distance=100)
        self.__myRobot.waitUntilFinishedDriving()

