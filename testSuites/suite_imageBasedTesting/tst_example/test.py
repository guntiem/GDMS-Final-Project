# -*- coding: utf-8 -*-
''' EXAMPLE:
    Walkthrough:
    Iterating through each icon against the expected result (all icons visible), the script will go through needed GUI interaction to 
    ensure that the icon display functionality works as needed. 
'''

import names
import datetime
import os
    
SCREEN = names.gDMS_Sample_Application_QQuickWindowQmlImpl

ICONS = ['alertIcon', 'headphoneIcon', 'lockedIcon', 'mutedIcon', 'pauseIcon', 'videoIcon', 'voicemailIcon']
# ICON_CHECKBOXES = {'alertIcon' : 'waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton',
#               'headphoneIcon' : 'waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton',
#               'mutedIcon' : 'waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton',
#               'pauseIcon' : 'waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton',
#               'videoIcon' : 'waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton',
#               'voicemailIcon' : 'waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton'}


def setup():
    # testSettings.logScreenshotOnError = True
    # testSettings.logScreenshotOnFail = True
    testSettings.reportFormat = "html"
              

def save_screenshot(filename):
    widget = waitForObject(SCREEN)
    img = object.grabScreenshot(widget)
    
    img.save(filename)
    testData.get(filename)
    
    screenshot_dir = '../testSuites/suite_imageBasedTesting/errorImages'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    full_path = os.path.join(screenshot_dir, filename)
    img.save(full_path)
    testData.get(full_path)
    
    
def main():
    global SCREEN, ICONS
    setup()
    
    #=== SETUP ==================================================================================================================
    # start application
    startApplication("appsampleApp")
    
    # entering relevant app page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    
    # displaying following icons onto the menubar section using GUI checkboxes...
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 12, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton)
    #============================================================================================================================
    

    #=== ICON TESTING ===========================================================================================================
    # Expected: All icons visible
    # Test: Iterate through all expected icons and check for visibility.
    # Actions: If icon not visible, ensure functionality for visibility works then test again. If total fail, capture screenshot.
    # *** for demonstration purposes, only some icons are visible at the beginning of testing procedure. 
    test.log("TESTING MENU ICONS...")
    
    for icon in ICONS:
        # initial check
        if test.imagePresent(icon, {'timeout': 5000, 'tolerant': True, 'multiscale': True, 'threshold': 99.5,
                                           'message': f'Test {icon} visibility: attempt 1'}, waitForObject(SCREEN)):
            test.log(f"Test {icon} visibility: PASS on attempt 1")
            
        # check action that leads to expected initial check
        else:
            for i in range(2,6):
                match icon:
                    case 'alertIcon' :
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 15, 15, Qt.LeftButton)
                    case 'headphoneIcon' : 
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 15, 4, Qt.LeftButton)
                    case 'lockedIcon' :
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 15, 16, Qt.LeftButton)
                    case 'mutedIcon' :
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 14, 14, Qt.LeftButton)   
                    case 'pauseIcon' : 
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 14, 8, Qt.LeftButton)
                    case 'videoIcon' : 
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 14, 11, Qt.LeftButton)
                    case 'voicemailIcon' :
                        mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 14, 19, Qt.LeftButton)
                
                if test.imagePresent(icon, {'timeout': 5000, 'tolerant': True, 'multiscale': True, 'threshold': 90.0,
                                            'message': f'Test {icon} visibility: attempt {i}'}):
                    test.log(f"Test {icon} visibility: PASS on attempt {i}")   
                    break
        
                # log a screenshot if overall test failure
                # if not findImage(icon, {'tolerant': True, 'multiscale': True, 'threshold': 99.5,
                                    # 'message': f'Test {icon}: Image was never identified. Logging screenshot'}, waitForObject(SCREEN)):
                now = datetime.datetime.now()
                date = now.strftime("%Y-%m-%d_%H:%M:%S")
                screenshot_name = f"{icon}_fail_{date}.png"
                save_screenshot(screenshot_name)
                test.fail(f"Test {icon}: FAIL after 5 attempts", f'Screenshot saved at {date}')
    #============================================================================================================================
        
    
    #=== TEXT TESTING ===========================================================================================================
    # Expected: Test for individual words, digits, and occurrences on screen
    # Tests: Region to test: entire screen 
    #    - Check for individual words
    #    - Check for expected string of words
    #    - Testing for "0123"
    #    - Testing for "0", "1", "2", and "3"
    # Actions: Check for visibility. If failure, reduce tolerance 3 times and test again. If total fail, capture screenshot.
    test.log("TESTING DISPLAYED TEXT ON SCREEN...")
    
    
    # SIMPLE SENTENCES 
    test.ocrTextPresent("This is Filler text to use to test the OCR engine's text", { "tesseract": { "psm": 3 } }, 
                        waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl));
    


    # LOWER/UPPER CASES 
    test.ocrTextPresent("CASE", { "tesseract": { "psm": 3 }, "occurrence" : 2, "message": f"Testing multiple instance recognition"});
    test.ocrTextPresent("UPPERCASE", {"message":"Testing UPPER case recognition"})
    test.ocrTextPresent("lowercase", {"message":"Testing lower case recognition"})
    test.ocrTextPresent("MiXeD cAsE", {"message":"Testing MiXeD case recognition"})
    
    test.ocrTextPresent("mixed case", {"message":"Testing letter case sensitivity"})
    
    
    # NUMBERS AND SPACING 
    # checking for concurrent digits
    test.ocrTextPresent("01234", {"message": "Expected PASS (regular digits 0-9)"})
    # test.ocrTextPresent("56789", {"message": "Expected FAIL (full-Width digits 0-9)"}) # Tesseract difficulty combining full width digits
    
    #testing for individual digits
    test.ocrTextPresent("1", {"message": "Testing substring sensitivity for [1]"})
    test.ocrTextPresent("2", {"message": "Testing substring sensitivity for [2]"})
    test.ocrTextPresent("3", {"message": "Testing substring sensitivity for [3]"})
    
                        
    # TEXT NOT PRESENT 
    test.ocrTextNotPresent("ASU", { "tesseract": { "psm": 3 }, 'message' : 'Testing for text not on display [ASU]'});
    test.ocrTextNotPresent("Squish", { "tesseract": { "psm": 3 }, 'message' : 'Testing for text not on display [Squish]'});
    test.ocrTextNotPresent("Capstone Project", { "tesseract": { "psm": 3 }, 'message' : 'Testing for text not on display [Capstone Project]'});
    
    
    # REDUCE TOLERANCE EXAMPLE
    test.ocrTextPresent("!@#$%^&*()_+-=[]{}|;:'\",.<>?/", {"message": "Expected all characters to match"})
    #============================================================================================================================
    
    
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)

