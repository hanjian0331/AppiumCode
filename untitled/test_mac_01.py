import pytest
import os
import copy

from appium import webdriver
import subprocess

class TestIOSSelectors():

    @pytest.fixture(scope='function')
    def driver(self, request):
        defaultLoopDelay_sec = 1.00
        defaultCommandDelay_sec = 0.100
        defaultImplicitTimeout_sec = 3.000
        defaultMouseSpeed = 300
        defaultScreenShotOnError = False
        defaultGlobalDiagnosticsDirectory = '~/Desktop/'
        defaultCookies = [
            {'name': 'loop_delay', 'value': defaultLoopDelay_sec},
            {'name': 'command_delay', 'value': defaultCommandDelay_sec},
            {'name': 'implicit_timeout', 'value': defaultImplicitTimeout_sec},
            {'name': 'mouse_speed', 'value': defaultMouseSpeed},
            {'name': 'screen_shot_on_error', 'value': defaultScreenShotOnError},
            {'name': 'global_diagnostics_directory', 'value': defaultGlobalDiagnosticsDirectory}
        ]
        desiredCapabilities = {'platform': 'Mac', 'cookies': defaultCookies}
        driver = webdriver.Remote(command_executor='http://localhost:4622/wd/hub',
                                  desired_capabilities=desiredCapabilities)
        driver.get("Calculator")

        def fin():
            driver.quit()
            subprocess.call(['osascript', '-e', 'tell application "Calculator" to quit'])

        request.addfinalizer(fin)

        driver.implicitly_wait(10)
        return driver

    def test_01(self, driver):
        print("1")

    def test_02(self, driver):
        print("2")
        