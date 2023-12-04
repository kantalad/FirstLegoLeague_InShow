#!/usr/bin/env pybricks-micropython

from pybricks.tools import wait
from threading import Thread

class MenuItem:

    def __init__(self, myRobot):
        self.myRobot = myRobot
        self.position = 0

    def setPosition(self, position=0):
        self.position = position

    def name(self):
        prefix = str(self.position)
        if self.position <= 0:
            return self.__class__.__name__

        if self.position <= 9:
            prefix = "0" + str(self.position)

        return prefix + ": " + self.__class__.__name__

    def go(self):
        print(self.name(),  " starting")
        self.__go()
        print(self.name(),  " finished")

    def __go(self):
        raise NotImplementedError
