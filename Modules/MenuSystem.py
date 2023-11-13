#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from threading import Thread


class MenuSystem:

    __ev3 = None
    __myRobot = None

    def __init__(self, ev3:ev3, myRobot:myRobot):
         self.__ev3 = ev3
         self.__myRobot = myRobot

    def start(self):
        self.__ev3.screen.print("Hello World!")
        wait(10000)
