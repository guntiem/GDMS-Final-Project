# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    - reduce screen area by object to reduce visual noise > increase OCR validity (https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
'''

import names


def findText(text):
    if test.ocrTextPresent(text, {"timeout": 1000}):
        test.passes(f"PASS: {text} text visible!")   
    else:
        screenshot_name = f"ocr_for_{text}_fail.png"
        save_screenshot(screenshot_name)
        
        test.log(f"Screenshot taken. Failed OCR verification for: {text}")
    return
        
    
def runTestRecording():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 42, 39, Qt.LeftButton)
    
    snooze(5) # NOTE: Need to include snooze after every GUI interaction for consisted expected output logging
    
    # Insert ocr text verification, and add logic to create the test pass/fail criteria
    findText("12345678") # can toggle for testing
    

def main():
    # setUp()
    # Register AUT with squishserver:
    # aut = "ThermostatApp"
    # path = os.path.join('/home/kadum/Qt/Examples/Qt-6.7.3/demos/thermostat/build/Desktop_Qt_6_7_3-Debug')
    # registerAUT(aut, path)
    
    runTestRecording()
