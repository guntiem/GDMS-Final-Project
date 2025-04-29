# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    > Screenshotting upon [Test fail, test pass, error, etc]
    > Separate logging without pass/fail criteria
'''
import names
import datetime
import os

SCREEN = names.gDMS_Sample_Application_QQuickWindowQmlImpl


def save_screenshot(test):
    global SCREEN
    widget = waitForObject(SCREEN)
    img = object.grabScreenshot(widget)
    
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d_%H:%M:%S")
    screenshot_name = f"{test}_fail_{date}.png"
    img.save(screenshot_name)
    
    screenshot_dir = '../../../testSuites/suite_imageBasedTesting/screenshots'
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    full_path = os.path.join(screenshot_dir, screenshot_name)
    img.save(full_path)
    testData.get(full_path)
        

def main():
    list_of_expected_words = ['UPPERCASE', 'lowercase', 'OCR']
    list_of_unexpected_words = ['ASU']
    
    #=== SETUP =========================================================================================================================
    startApplication("appsampleApp")
    
    # entering OCR testing page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    #===================================================================================================================================
    
    
    #=== TEST SETTINGS =================================================================================================================
    # Squish's global testSettings properties include screenshot functionalities along with other useful test execution settings. 
    # Enabling the properties below automatically applies implied functions. 
    # Ref; https://doc.qt.io/squish/rgs-testsettings.html
    
    # testSettings.logScreenshotOnError = True
    # testSettings.logScreenshotOnFail = True
    # testSettings.logScreenshotOnPass = True
    # testSettings.logScreenshotOnWarning = True
    
    # testSettings.reportFormat = "html"
    #===================================================================================================================================
    
    
    #=== CUSTOM ERROR LOGGING ==========================================================================================================
    # imagePresent() and imageNotPresent() 'message' argument is logged regardless of pass/fail result
    # ^ Same applies to ocrTextPresent() and ocrTextNotPresent()
    
    test.log('ENTER Custom Error Logging...')
    
    for word in list_of_expected_words:
        test.ocrTextPresent(word, { "tesseract": { "psm": 3 }, 'message' : f"Test for \"{word}\" visibility"});
    
    test.log('Example message using test.log() function', 'Example detail using test.log() function')
    test.passes('Example message using test.passes() function', 'Example detail using test.passes() function')
    test.fail('Example message using test.fail() function', 'Example detail using test.fail() function')
    
    test.log('EXIT Custom Error Logging.')
    #===================================================================================================================================
    
    
    #=== SIMPLE SCREENSHOT BEHAVIOR ====================================================================================================
    # Along with Squish's built in screenshot upon failure/pass/etc functionalities, we can also grab screenshots of the application
    # at other points of execution if needed. Below is an example of how this can be done:
    
    test.log('ENTER Screenshot Methods...')
    
    for word in list_of_unexpected_words:
        
        # PASS example: Creating custom screenshot function
        if test.ocrTextNotPresent(word, { "tesseract": { "psm": 3 }, 'message': f"custom_testID-01234: Locating \"{word}\""}):
            save_screenshot(word)
            test.log("custom_testID_01234: Screenshot taken", 'Custom Screenshot')
    
        # FAIL example: Using findOcrText()
        testSettings.logScreenshotOnError = True
        try:
            findOcrText(word, {"tesseract": { "psm": 3 }, 'message': f"logOnError_testID-01235: Locating \"{word}\""}) 
        except:
            test.log(f"logOnError_testID-01235: Screenshot taken.", 'logScreenshotOnError example')
        testSettings.logScreenshotOnError = False
        
        # FAIL/PASS example: Utilizing testSettings (Saved to .squish/Test Results)
        testSettings.logScreenshotOnFail = True
        test.ocrTextPresent(word, { "tesseract": { "psm": 3 }, 'timeout': 5000, 'message': f"logOnFail_testID-01236: Locating \"{word}\""})
        testSettings.logScreenshotOnFail = False
            
    test.log('EXIT Simple Screenshot Examples.')
    #===================================================================================================================================
    
    
    closeWindow(SCREEN)
