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
    
    screenshot_dir = '/home/kadum/GDMS-Final-Project/testSuites/suite_imageBasedTesting'
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


# Sample usage of full display testing using saved image files from local saved directory                                                                                               # This is 
def verifyMenuIcon(icon_name):
    test.imagePresent(f'{icon_name}', {'tolerant': True, 
                                       'multiscale': True, 
                                       'threshold': 99.5})
    
    
def runApplication():
    startApplication("appsampleApp")
    
    # Entering relevant App page
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    
    # displaying all icons available 
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 12, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton)


def main():
    runApplication()
    
    findText("12345678")
    
    verifyMenuIcon("mutedIcon")
    verifyMenuIcon("pauseIcon")
    verifyMenuIcon("videoIcon")
