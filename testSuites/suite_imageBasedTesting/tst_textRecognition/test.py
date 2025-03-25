# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    - test.ocrTextPresent(): test for visual text recognition.  Ref: https://doc.qt.io/squish/test-ocrtextpresent-function.html
        > returns bool
        > arguments
        > passes when first argument passed (text to test value) is recognized in app screen
        - ParameterMap: {'parameter' : 'value', ...}
            > ParameterMap for test,imagePresent include: occurrence, interval, timeout, tolerant, threshold, multiscale, minScale, maxScale, message
        - Region to test can be specified via display bounds or QtApplication object
    - reduce screen area by object to reduce visual noise > increase OCR validity (https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
'''

import names


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
    test.ocrTextPresent("I@#$%*&*()_+-=[]{}|;:\"\",.<>?/", {}, 
                        waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl));
                        
    
    
    # ===============================================================================================================================
    
    # ===============================================================================================================================
    
    
    
    #=== APPLICATION GUI INTERACTION SETUP =========================================================================================
    startApplication("appsampleApp")
    
    # entering relevant App page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    #============================================================================================================================
    
    
    #=== BASIC IMAGE PRESENT/NOT PRESENT TESTING (ALL PASS) ======================================================================
    # this approach utilizes the entire window screen to check for icon presence
    test.imagePresent("headphoneIcon")
    test.imagePresent("mutedIcon")
    test.imagePresent("alertIcon")
    test.imagePresent("lockedIcon")
    
    test.imageNotPresent("pauseIcon")
    test.imageNotPresent("videoIcon")
    test.imageNotPresent("voicemailIcon")
    #===============================================================================================================================
    
    
    #=== TUNING PARAMETERS (ALL PASS)===============================================================================================
    # tolerant: 
    # multiscale: 
    # threshold: 
    test.imagePresent('mutedIcon', {'tolerant': True, 'multiscale': True, 'threshold': 99.5},)
    #===============================================================================================================================
    
    
    #=== TESTING SPECIFIC WINDOW REGION (ALL PASS) =================================================================================
    # Specify by Ratio: This approach utilizes the entire window screen to check for icon presence
    BOUNDS = object.globalBounds(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
    BOUNDS.width = BOUNDS.width / 2
    test.imageNotPresent('mutedIcon', {}, BOUNDS) # Will check the 2nd and 3rd quadrants
    
    # Specify by Pixels: using UiTypes.ScreenRectangle(x, y, width, height)
    # NOTE: The display screen size for this test case is 850x480
    test.imagePresent('mutedIcon', {'tolerant': False}, UiTypes.ScreenRectangle(630, 0, 220, 40)) # Only the area of the screen if max(iconsPresent)
    #===============================================================================================================================
    
    
    #=== TESTING SPECIFIC OBJECT BOUNDS (ALL PASS) =================================================================================
    # The following will grab region spanned by QtApp objects
    test.imagePresent("mutedIcon", {}, waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem))
    
    # NOTE: You can also list multiple objects, pass as a list. 
    test.imagePresent("mutedIcon", {}, [waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem), 
                                        waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting)])
    #===============================================================================================================================
    
    
    
    
    

    
    

