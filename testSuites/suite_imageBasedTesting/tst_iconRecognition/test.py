# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    - test.ImagePresent(): test for icons/images.  Ref: https://doc.qt.io/squish/squish-api.html#findimage-function
        > returns bool
        > passes test when image is found. On the other hand, test.ImageNotPresent() passes when image given disappears from screen.
        - ParameterMap: {'parameter' : 'value', ...}
            > ParameterMap for test,imagePresent include: occurrence, interval, timeout, tolerant, threshold, multiscale, minScale, maxScale, message
        - Region to test can be specified via display bounds or QtApplication object
'''
import names
    
def main():
    
    # === APPLICATION GUI INTERACTION SETUP =========================================================================================
    startApplication("appsampleApp")
    
    # Entering relevant App page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    
    # Displaying following icons onto the menubar section using GUI checkboxes...
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 12, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton)
    
    # Leave these icons hidden...
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton)
    # mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton)
    # ============================================================================================================================
    
    
    # === BASIC IMAGE PRESENT/NOT PRESENT TESTING (ALL PASS) ======================================================================
    # This approach utilizes the entire window screen to check for icon presence
    test.imagePresent("headphoneIcon")
    test.imagePresent("mutedIcon")
    test.imagePresent("alertIcon")
    test.imagePresent("lockedIcon")
    
    test.imageNotPresent("pauseIcon")
    test.imageNotPresent("videoIcon")
    test.imageNotPresent("voicemailIcon")
    # ===============================================================================================================================
    
    
    # === TUNING PARAMETERS (ALL PASS)===============================================================================================
    # tolerant: 
    # multiscale: 
    # threshold: 
    test.imagePresent('mutedIcon', {'tolerant': True, 'multiscale': True, 'threshold': 99.5},)
    # ===============================================================================================================================
    
    
    # === TESTING SPECIFIC WINDOW REGION (ALL PASS) =================================================================================
    # Specify by Ratio: This approach utilizes the entire window screen to check for icon presence
    BOUNDS = object.globalBounds(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
    BOUNDS.width = BOUNDS.width / 2
    test.imageNotPresent('mutedIcon', {}, BOUNDS) # Will check the 2nd and 3rd quadrants
    
    # Specify by Pixels: using UiTypes.ScreenRectangle(x, y, width, height)
    # NOTE: The display screen size for this test case is 850x480
    test.imagePresent('mutedIcon', {'tolerant': False}, UiTypes.ScreenRectangle(630, 0, 220, 40)) # Only the area of the screen if max(iconsPresent)
    # ===============================================================================================================================
    
    
    # === TESTING SPECIFIC OBJECT BOUNDS (ALL PASS) =================================================================================
    # The following will grab region spanned by QtApp objects
    test.imagePresent("mutedIcon", {}, waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem))
    
    # NOTE: You can also list multiple objects, pass as a list. 
    test.imagePresent("mutedIcon", {}, [waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem), 
                                        waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting)])
    # ===============================================================================================================================
    
    
    
    
    

    
    
