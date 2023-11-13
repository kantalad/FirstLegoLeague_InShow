#!/usr/bin/env pybricks-micropython

class M04_Masterpiece:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def go(self):
        self.__myRobot.drive(speed=100, distance=100)
        self.__myRobot.waitUntilFinishedDriving()

        self.__myRobot.frontUntilStalled(speed=-360)
        self.__myRobot.frontUntilTarget(target_angle=0, wait=True)

        self.__myRobot.driveBackwards(speed=100, distance=100)
        self.__myRobot.waitUntilFinishedDriving()
