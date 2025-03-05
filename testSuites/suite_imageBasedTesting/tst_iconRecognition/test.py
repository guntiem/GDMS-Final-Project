# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    - test.ImagePresent(): test for icons/images.  Ref: https://doc.qt.io/squish/squish-api.html#findimage-function
        > returns bool
        > passes test when image is found. On the other hand, test.ImageNotPresent() passes when image given disappears from screen.
        - ParameterMap: {'parameter' : 'value', ...}
            > ParameterMap for test,imagePresent include: occurrence, interval, timeout, tolerant, threshold, multiscale, minScale, maxScale, message
        - Region to test can be specified via display bounds or QtApplication object
            - via Bounds:
                > Declared regions begin from the top-left corner of the window
            - via Objects:
                - 
'''
import names
    
def runTests():
    verifyMenuIcon("mutedIcon")
    verifyMenuIcon("pauseIcon")
    verifyMenuIcon("videoIcon")
    verifyMenuIcon("voicemailIcon")
    verifyMenuIcon("pauseIcon")


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
    # ===============================================================================================================================
    
    BOUNDS = object.globalBounds(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
    UPPER_RIGHT = BOUNDS

    UPPER_RIGHT.width = BOUNDS.width / 2
    
    # === BASIC IMAGE PRESENT TESTING (ALL PASS) ====================================================================================
    # This approach utilizes the entire window screen to check for icon presence
    test.imagePresent("headphoneIcon")
    test.imagePresent("mutedIcon")
    test.imagePresent("alertIcon")
    test.imagePresent("lockedIcon")
    # ===============================================================================================================================
    
    
    # === TESTING SPECIFIC WINDOW REGION (ALL PASS) =================================================================================
    # This approach utilizes the entire window screen to check for icon presence
    test.imagePresent('mutedIcon', {'tolerant': True, 'multiscale': True, 'threshold': 99.5}, BOUNDS)
    # ===============================================================================================================================
    
    
    
    
    

    
    
