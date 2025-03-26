# -*- coding: utf-8 -*-

import names


def main():
    #Start Application
    startApplication("appsampleApp")
    
    #Click on Settings Screen
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 52, 40, Qt.LeftButton)
    
    #Single Click
    mouseClick(waitForObject(names.security_Settings_Button), 95, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.security_Settings_Button), 95, 11, Qt.LeftButton)
    test.log("Single Click: Button not working")
    
    #Double Click
    doubleClick(waitForObject(names.security_Settings_Button), 95, 11, Qt.LeftButton)
    doubleClick(waitForObject(names.security_Settings_Button), 95, 11, Qt.LeftButton)
    test.log("Double Click: Button not working")
    
    longMouseClick(waitForObject(names.security_Settings_Button), 76, 15, Qt.LeftButton)
    test.compare(waitForObject(names.security_Settings_Button).visible, True, "Pop-up should be visible after long press")

    
    #Close pop up
    mouseClick(waitForObject(names.close_Button), 24, 16, Qt.LeftButton)
    test.passes("Test Case Passed: Long Press Functionality works")
