#!/usr/bin/env pybricks-micropython

from pybricks.media.ev3dev import Font
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from threading import Thread


class MenuSystem:

    def __init__(self, ev3:ev3):
        self.ev3 = ev3

        self.font = Font(family=None, size=16, bold=False, monospace=False, lang=None, script=None)
        self.ev3.screen.set_font(self.font)

        self.menuItems = []
        self.currentIndex = 0

    def addItem(self, item:item):
        count = len(self.menuItems)
        item.setPosition(position=count + 1)
        self.menuItems.append(item)

    def go(self):
        print("menu running")
        while True:

            pressed = self.ev3.buttons.pressed()
            if Button.CENTER in pressed:
                print("center button pressed")
                self.menuItems[self.currentIndex].go()

            elif Button.UP in pressed:
                print("up button pressed")
                if 0 < self.currentIndex:
                    self.currentIndex = self.currentIndex - 1

            elif Button.DOWN in pressed:
                print("down button pressed")
                if self.currentIndex < (len(self.menuItems) - 1):
                    self.currentIndex = self.currentIndex + 1

            self.__draw()

            wait(125)

    def __draw(self):
        #print("refresh screen")
        self.ev3.screen.clear()

        startIndex = self.__startIndex()
        endIndex = self.__endIndex()

        offset = -1
        for x in range(startIndex, endIndex):
            #print("start index: ", startIndex, " end index: ", endIndex, " x: ", x)

            item = self.menuItems[x]
            offset = offset + 1

            if self.currentIndex == x:
                self.ev3.screen.draw_text(0, offset*16, item.name(), text_color=Color.WHITE, background_color=Color.BLACK)
            else:
                self.ev3.screen.draw_text(0, offset*16, item.name(), text_color=Color.BLACK, background_color=Color.WHITE)


    def __startIndex(self):

        count = len(self.menuItems) 
        if(count <= 8):
            return 0

        index = self.currentIndex - 4        
        if(index < 0):
            return 0

        count = len(self.menuItems) 
        if((count - 8) < index):
            return count - 8

        return index


    def __endIndex(self):
        index = self.currentIndex + 4
        count = len(self.menuItems) 

        if(count <= 8):
            return count

        if(count < index):
            return count

        if(index <= 8):
            return 8

        return index
