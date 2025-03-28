# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    > Screenshotting upon [Test fail, test pass, error]
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
    list_of_expected_words = ['UPPERCASE', 'lowercase', 'uppercase']
    # list_of_unexpected_words = ['ASU', 'Capstone']
    
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
    
    test.log('ENTER Simple Screenshot Examples...')
    
    # PASS example: Creating custom screenshot function
    for word in list_of_expected_words:
        if not test.ocrTextPresent(word, { "tesseract": { "psm": 3 } }):
            test.log(f'Failed to locate {word}. Taking screenshot...', 'Image saved in: ../../../testSuites/suite_imageBasedTesting/screenshots')
            save_screenshot(word)
            
    
    # FAIL example: Using findOcrText()
    # testSettings.logScreenshotOnError = True
    # findOcrText('ASU', { "tesseract": { "psm": 3 } });
    # testSettings.logScreenshotOnError = False
    
    # FAIL example: Utilizing testSettings (Saved to .squish/Test Results)
    testSettings.logScreenshotOnFail = True
    test.ocrTextPresent("ASU", { "tesseract": { "psm": 3 }, 'timeout': 5000})
    testSettings.logScreenshotOnFail = False
    
    # FAIL example: Custom screenshot saving
    if not test.ocrTextPresent("ASU", { "tesseract": { "psm": 3 }, 'timeout': 5000}):
        test.log(f'Failed to locate {word}. Taking screenshot...', 'Image saved in: ../../../testSuites/suite_imageBasedTesting/screenshots')
        save_screenshot(word)
        
    test.log('EXIT Simple Screenshot Examples.')
    #===================================================================================================================================
    
    
    closeWindow(SCREEN)
