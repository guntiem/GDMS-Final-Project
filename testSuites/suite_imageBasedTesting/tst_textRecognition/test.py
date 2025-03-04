# -*- coding: utf-8 -*-
''' NOTES:
    - reduce screen area by object to reduce visual noise > increase OCR validity (https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
'''

import names


def findText(text):
    if test.ocrTextPresent(text, {"timeout": 1000}):
        test.passes(f"PASS: {text} text visible!")   
    else:
        screenshot_name = f"ocr_for_{text}_fail.png"
        save_screenshot(screenshot_name)
        
        test.log(f"Screenshot taken. Failed OCR verification: {text}")
        
    return
        
    
def runTestRecording():
    startApplication("appsampleApp")
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
