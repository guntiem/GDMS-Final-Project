# -*- coding: utf-8 -*-
''' NOTES:
    - reduce screen area by object to reduce visual noise > increase OCR validity (https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
'''

import names
import os.path
import sys

def setUp():
    testSettings.logScreenshotOnError = True
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnWarning = True
    testSettings.logScreenshotOnPass = True
    testSettings.reportFormat = "html"  # or "xml" for XML reports
    testSettings.reportDir = "/home/kadum"


# TODO: not yet used
def registerAUT(aut, path, squishserver_host=None, squishserver_port=None):
    s = '"' + os.environ["SQUISH_PREFIX"] + '/bin/squishrunner"'
    if squishserver_host is not None:
        s += ' --host ' + squishserver_host
    if squishserver_port is not None:
        s += ' port=' + str(squishserver_port)
    s += ' --config addAUT "' + aut + '" "' + path + '"'
    if sys.platform == "win32" and s.endswith('"'):
        s = '"' + s
    test.log("Executing: " + s)
    os.system(s)
    

def save_screenshot(filename):
    widget = waitForObject(names.thermostat_QQuickWindowQmlImpl)
    img = object.grabScreenshot(widget)
    
    # img.save(filename)
    # testData.get(filename)
    
    screenshot_dir = '/home/kadum/GDMS-Capstone/suite_ocr_testing/tst_screenshotting'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    full_path = os.path.join(screenshot_dir, filename)
    img.save(full_path)
    testData.get(full_path)


def findText(text):
    if test.ocrTextPresent(text, {"timeout": 1000}):
        test.passes(f"PASS: {text} text visible!")   
    # elif test.ocrTextNotPresent(text, {"timeout": 2000}): # "timeout" parameter time in ms
    #     test.fail(f"FAIL: Failed to find the text {text} on screen.")
        
        # saving screenshot on fail point
        #screenshot_name = f"{text}_ocrfail"
        #save_screenshot(screenshot_name)
    else:
        # saving screenshot on fail point
        screenshot_name = f"ocr_for_{text}_fail.png"
        save_screenshot(screenshot_name)
        
        test.log(f"Screenshot taken. Failed OCR verification: {text}")
        
    return
        
    
def runTestRecording():
    startApplication("ThermostatApp")
    mouseWheel(waitForObject(names.scrollView_toggle_CustomSwitch), 19, 35, 0, -30, Qt.NoModifier)
    mouseWheel(waitForObject(names.scrollView_Flickable), 494, 57, 0, -735, Qt.NoModifier)
    snooze(5) # NOTE: Need to include snooze after every GUI interaction for consisted expected output logging
    
    # Insert ocr text verification, and add logic to create the test pass/fail criteria
    findText("Kitchen") # can toggle for testing
    findText("Bedroom")
    findText("capstone")
    
    closeWindow(names.thermostat_QQuickWindowQmlImpl)


def main():
    # setUp()
    # Register AUT with squishserver:
    # aut = "ThermostatApp"
    # path = os.path.join('/home/kadum/Qt/Examples/Qt-6.7.3/demos/thermostat/build/Desktop_Qt_6_7_3-Debug')
    # registerAUT(aut, path)
    
    runTestRecording()
