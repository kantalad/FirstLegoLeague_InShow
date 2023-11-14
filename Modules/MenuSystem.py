#!/usr/bin/env pybricks-micropython

from pybricks.media.ev3dev import Font
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from threading import Thread


class MenuSystem:

    __ev3 = None
    __myRobot = None

    __font = Font(family=None, size=16, bold=False, monospace=False, lang=None, script=None)

    __menuItems = []
    __currentIndex = 0

    def __init__(self, ev3:ev3, myRobot:myRobot):
        self.__ev3 = ev3
        self.__myRobot = myRobot
        self.__ev3.screen.set_font(self.__font)

    def addItem(self, item:item):
        self.__menuItems.append(item)

    def start(self):
        print("starting menu")
        while True:

            pressed = self.__ev3.buttons.pressed()
            if Button.CENTER in pressed:
                print("center button pressed")
                self.__menuItems[self.__currentIndex].go()

            elif Button.UP in pressed:
                print("up button pressed")
                if 0 < self.__currentIndex:
                    self.__currentIndex = self.__currentIndex - 1

            elif Button.DOWN in pressed:
                print("down button pressed")
                if self.__currentIndex < (len(self.__menuItems) - 1):
                    self.__currentIndex = self.__currentIndex + 1

            self.__draw()

            wait(125)

    def __draw(self):
        #print("refresh screen")
        self.__ev3.screen.clear()

        startIndex = self.__startIndex()
        endIndex = self.__endIndex()

        offset = -1
        for x in range(startIndex, endIndex):
            print("start index: ", startIndex, " end index: ", endIndex, " x: ", x)

            item = self.__menuItems[x]
            offset = offset + 1

            if self.__currentIndex == x:
                self.__ev3.screen.draw_text(0, offset*16, item.name(), text_color=Color.WHITE, background_color=Color.BLACK)
            else:
                self.__ev3.screen.draw_text(0, offset*16, item.name(), text_color=Color.BLACK, background_color=Color.WHITE)


    def __startIndex(self):
        index = self.__currentIndex - 4
        if(index < 0):
            return 0

        count = len(self.__menuItems) 
        if((count - 8) < index):
            return count - 8

        return index

    def __endIndex(self):
        index = self.__currentIndex + 4
        count = len(self.__menuItems) 

        if(count <= 8):
            return count

        if(count < index):
            return count

        if(index <= 8):
            return 8

        return index
