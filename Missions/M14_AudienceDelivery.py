#!/usr/bin/env pybricks-micropython

class M14_AudienceDelivery:

    __myRobot = None

    def __init__(self, myRobot):
        self.__myRobot = myRobot

    def name(self):
        return "M14: Audience Delivery"

    def go(self):
        self.__myRobot.driveUntilBump()
        self.__myRobot.waitUntilFinishedDriving()

