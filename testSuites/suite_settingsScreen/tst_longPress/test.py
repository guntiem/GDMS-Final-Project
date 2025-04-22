# -*- coding: utf-8 -*-

import names
import time

def main():
    #Start Application
    # startApplication("appsampleApp")
    attachToApplication("appsampleApp")
    
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
    
    # longMouseClick(waitForObject(names.security_Settings_Button), 76, 15, Qt.LeftButton)
    # test.compare(waitForObject(names.security_Settings_Button).visible, True, "Pop-up should be visible after long press")
    
    if object.exists(names.security_Settings_Button):
        #btn = waitForObject(names.security_Settings_Button)
        mousePress(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)
        time.sleep(1.5)
        mouseRelease(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)

        # test.compare(btn.visible, True, "Pop-up should be visible after long press")
        test.compare(waitForObjectExists(names.o_Rectangle_6).visible, True)

        mouseClick(waitForObject(names.close_Button), 24, 16, Qt.LeftButton)
        test.passes("Test Case Passed: Long Press Functionality works")
    else:
        test.fail("security_Settings_Button does not exist.")

    
    #Close pop up
    # mouseClick(waitForObject(names.close_Button), 24, 16, Qt.LeftButton)
    # test.passes("Test Case Passed: Long Press Functionality works")
    
    # Remove later(?) - Tony
    mouseWheel(waitForObject(names.o_Flickable), 507, 280, 0, -180, Qt.NoModifier)
    mouseClick(waitForObject(names.back_Button), 66, 14, Qt.LeftButton)
