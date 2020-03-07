#coding=utf-8

from selenium.webdriver.remote.webelement import *

class Page:

    def __init__(self, driver):
        self.driver = driver

    def findElementByPath(self, path):
        # type: (str) -> WebElement
        return self.driver.find_element_by_xpath(path)