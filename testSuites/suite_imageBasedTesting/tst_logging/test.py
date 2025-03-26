# -*- coding: utf-8 -*-

import names

def save_screenshot(filename):
    widget = waitForObject(names.thermostat_QQuickWindowQmlImpl)
    img = object.grabScreenshot(widget)
    
    # img.save(filename)
    # testData.get(filename)
    
    screenshot_dir = '../testSuites/suite_imageBasedTesting'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    full_path = os.path.join(screenshot_dir, filename)
    img.save(full_path)
    testData.get(full_path)


def findText(text):
    if test.ocrTextPresent(text, {"timeout": 1000}):
        test.passes(f"PASS: {text} text visible!")   
    else:
        screenshot_name = f"ocr_for_{text}_fail.png"
        save_screenshot(screenshot_name)
        
        test.log(f"Screenshot taken. Failed OCR verification for: {text}")
    return

def findImage(image):
    if test.ocrTextPresent(text, {"timeout": 1000}):
        test.passes(f"PASS: {image} icon visible!")   
    else:
        screenshot_name = f"ocr_for_{image}_fail.png"
        save_screenshot(screenshot_name)
        
        test.log(f"Screenshot taken. Failed to find {image}")
    return
        
    
def runTestRecording():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 42, 39, Qt.LeftButton)
    
    snooze(5) # NOTE: Need to include snooze after every GUI interaction for consisted expected output logging
    
    # Insert ocr text verification, and add logic to create the test pass/fail criteria
    findText("12345678") # can toggle for testing
    

def main():
    startApplication("appsampleApp")
    
    #=== SIMPLE SCREENSHOTING BEHAVIOR ===============================================================================================
    # there are multiple ways to modify custom error logging here 
    test.imagePresent('mutedIcon', {'message': 'this can export a string saying mutedIcon image is visible'},)
    #===============================================================================================================================
    
    
    #=== CUSTOM ERROR LOGGING ===============================================================================================
    # there are multiple ways to modify custom error logging here
    test.imagePresent('mutedIcon', {'message': 'this can export a string saying mutedIcon image is visible'},)
    #===============================================================================================================================
    
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
