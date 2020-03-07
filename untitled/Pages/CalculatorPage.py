#coding=utf-8

from Page import *

windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
resultGroupPath = windowPath + "/AXGroup[0]"
basicGroupPath = windowPath + "/AXGroup[1]"
scientificGroupPath = windowPath + "/AXGroup[2]"
programmerGroupPath = windowPath + "/AXGroup[1]"


class CalculatorPage(Page):

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.clearButton = self.findElementByPath(basicGroupPath + "/AXButton[@AXDescription='clear']")





