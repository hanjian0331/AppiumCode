#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from random import randint
from Pages.CalculatorPage import *

print 'Starting the WebDriver session'
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


print 'Opening the "Calculator" app'
driver.get("Calculator")

caculatorPage = CalculatorPage(driver)
ActionChains(driver).move_to_element(caculatorPage.clearButton).perform()
caculatorPage.do_some_calculations_with_clicks()



# quit the webdriver instance
print 'Quitting the WebDriver session'
driver.quit()