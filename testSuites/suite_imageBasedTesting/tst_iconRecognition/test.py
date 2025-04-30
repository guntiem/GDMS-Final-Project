# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    > test.ImagePresent(): test for icons/images.  Ref: https://doc.qt.io/squish/squish-api.html#findimage-function
        - returns bool: True when image is found. On the other hand, test.ImageNotPresent() passes when image given disappears from screen.
        - arguments: imageFile, [parameterMap], [searchRegion]
        > parameterMap: {'parameter' : 'value', ...}
            - parameters: occurrence, interval(ms), timeout(ms), tolerant(bool), threshold, multiscale, minScale, maxScale, message
            
    > region to test can be specified via display bounds or QtApplication object
'''
import names
    
def main():
    #=== APPLICATION GUI INTERACTION SETUP =========================================================================================
    startApplication("appsampleApp")
    # attachToApplication("appsampleApp")
    
    # entering relevant app page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    
    # displaying following icons onto the menubar section using GUI checkboxes...
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 12, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton)
    
    # leave these icons hidden...
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton)
    #============================================================================================================================
    
    
    #=== BASIC IMAGE PRESENT/NOT PRESENT TESTING (all pass) ======================================================================
    # this approach utilizes the entire window screen to check for icon presence
    
    test.imagePresent("headphoneIcon")
    test.imagePresent("mutedIcon")
    test.imagePresent("alertIcon")
    test.imagePresent("lockedIcon")
    
    test.imageNotPresent("pauseIcon")
    test.imageNotPresent("videoIcon")
    test.imageNotPresent("voicemailIcon")
    #===============================================================================================================================
    
    
    #=== TEST VIA SPECIFIC REGION (all pass) =================================================================================
    # specify by ratio: this approach utilizes the entire window screen to check for icon presence
    #*** In this project, dividing ScreenRectangle area by more than 4 creates inconsistencies 

    BOUNDS = object.globalBounds(waitForObject(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem))
    
    # specify by pixels: using UiTypes.ScreenRectangle(x, y, width, height)
    test.imagePresent('mutedIcon', {'tolerant': True, 'multiscale': True, 'threshold': 99.5}, 
                      UiTypes.ScreenRectangle((BOUNDS.width / 4) * 3, 0, BOUNDS.width / 4, BOUNDS.height / 4)) 
    #===============================================================================================================================
    
    
    #=== TEST VIA OBJECT BOUNDS (all pass) =================================================================================
    # the following will grab region spanned by QtApp objects
    test.imagePresent("mutedIcon", {}, waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem))
    
    # ***you can also list multiple objects, pass as a list. 
    test.imagePresent("mutedIcon", {}, [waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem), 
                                        waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting)])
    #===============================================================================================================================
    
    
    #=== TUNING PARAMETERS (all pass) ===============================================================================================
    # tolerant: bool. Some differences between template image and actual display screenshot are allowed
    # multiscale: bool. Enables image search with scaling allowed
    # threshold: percentage value. Higher values are considered more exact match. (correlation percentage)
    
    test.imagePresent('mutedIcon', {'tolerant': True, 'multiscale': True, 'threshold': 99.5},)
    #===============================================================================================================================
    
    # closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)

