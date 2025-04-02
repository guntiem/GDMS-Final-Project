# -*- coding: utf-8 -*-

import names


def main():
    # startApplication("appsampleApp")
    attachToApplication("appsampleApp")
    # Compare home text to confirm user is on home page
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_Home_Text).text), "Home")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 37, 46, Qt.LeftButton)
    # Compare lock screen text to confirm user is on lock page
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_Screen_is_locked_Text).text), "Screen is locked.", "Phone has successfully been locked.")
    mouseClick(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), 145, 27, Qt.LeftButton)
    # Enter text and verify keyboard input and text on screen are equal
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "abcdefg")
    snooze(0.25)
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_passwordField_TextField).displayText), "abcdefg", "Text in textfield correctly reflects user keyboard input.")
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 52, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.oK_Button), 57, 15, Qt.LeftButton)
    snooze(1)
    # Confirm user is still on lock screen after incorrect password attempt
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_Screen_is_locked_Text).text), "Screen is locked.")
    mouseClick(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), 164, 29, Qt.LeftButton)
    # Enter correct password and compare keyboard input with on screen text
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "1234")
    snooze(0.25)
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_passwordField_TextField).displayText), "1234")
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 60, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.oK_Button), 57, 15, Qt.LeftButton)
    # Confirm that user returns to home page after unlocking phone
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_Home_Text).text), "Home")
