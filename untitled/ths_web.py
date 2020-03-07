#coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from random import randint
from Pages.CalculatorPage import *


defaultLoopDelay_sec = 1.00
defaultCommandDelay_sec = 0.100
defaultImplicitTimeout_sec = 3.000
defaultMouseSpeed = 300
defaultScreenShotOnError = False
defaultGlobalDiagnosticsDirectory = '~/Desktop/'
defaultCookies = [
    {'name': 'loop_delay', 'value': defaultLoopDelay_sec},
    {'name': 'command_delay', 'value':defaultCommandDelay_sec },
    {'name': 'implicit_timeout', 'value': defaultImplicitTimeout_sec},
    {'name': 'mouse_speed', 'value': defaultMouseSpeed},
    {'name': 'screen_shot_on_error', 'value': defaultScreenShotOnError},
    {'name': 'global_diagnostics_directory', 'value': defaultGlobalDiagnosticsDirectory}
]
desiredCapabilities = {'platform': 'Mac', 'cookies': defaultCookies}
# desiredCapabilities = {'platform':'Mac', 'commandDelay':50, 'loopDelay':1000, 'implicitTimeout':utilities.defaultImplicitTimeout_sec * 1000, 'mouseMoveSpeed':50, "screenShotOnError":1}
driver = webdriver.Remote(command_executor='http://localhost:4622/wd/hub', desired_capabilities=desiredCapabilities)
driver.get("同花顺")

path = "/AXApplication[@AXTitle='同花顺']/AXWindow[0]/AXButton[4]"
xuanGuButton = driver.find_element_by_xpath(path)

ac = ActionChains(driver)
# ac.move_to_element(xuanGuButton).click().perform()
# ac.move_to_element(driver.find_element_by_xpath("/AXApplication[@AXTitle='同花顺']/AXWindow[@AXIdentifier='_NS:100' and @AXSubrole='AXStandardWindow']/AXGroup[0]/AXGroup[0]/AXScrollArea[0]/AXWebArea[0]/AXButton[@AXDOMIdentifier='qs-enter' and @AXSubrole='AXSearchField']")).click().perform()
tf = driver.find_element_by_xpath("/AXApplication[@AXTitle='同花顺']/AXWindow[@AXIdentifier='_NS:100' and @AXSubrole='AXStandardWindow']/AXToolbar[0]/AXGroup[0]/AXTextField[0]")

ac.move_to_element(tf).click().send_keys(u'3韩').perform()
driver.quit()# quit the webdriver instance
