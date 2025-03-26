# -*- coding: utf-8 -*-
''' EXAMPLE:
    Walkthrough:
    Iterating through each icon against the expected result (all icons visible), the script will go through needed GUI interaction to 
    ensure that the icon display functionality works as needed. 
'''
import names
    
SCREEN = names.gDMS_Sample_Application_QQuickWindowQmlImpl
    
def main():
    global SCREEN
    
    
    #=== SETUP ==================================================================================================================
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

    #============================================================================================================================
    
    
    #=== TEXT TESTING ===========================================================================================================
    # Expected: Test for individual words, digits, and occurrences on screen
    # Tests: Region to test: entire screen 
    #    - Check for individual words
    #    - Check for expected string of words
    #    - Testing for "0123"
    #    - Testing for "0", "1", "2", and "3"
    # Actions: Check for visibility. If failure, reduce tolerance 3 times and test again. If total fail, capture screenshot.
    
    #============================================================================================================================
    
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)

