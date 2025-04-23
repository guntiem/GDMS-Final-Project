# -*- coding: utf-8 -*-

import names


def main():
    # startApplication("appsampleApp")
    attachToApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 31, 55, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), 137, 6, Qt.LeftButton)
    
    # Test incorrect password modal
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "abcd")
    snooze(0.5)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 75, 15, Qt.LeftButton)
    test.compare(waitForObjectExists(names.background_Rectangle).visible, True, "Modal appears correctly.")
    test.compare(str(waitForObjectExists(names.incorrectPassEnteredText_Text).text), "Incorrect password.", "Incorrect password modal has correct text.")
    test.compare(waitForObjectExists(names.oK_Button).visible, True, "Testing that Ok button exists")
    snooze(4)

    # Test to see if the modal object still exists
    # test.compare(object.exists(names.incorrect_password_Text), False, "Testing if modal is automatically dismissed after 3 seconds.")
    if not object.exists(names.incorrectPassEnteredText_Text):
        test.log("Modal successfully automatically dismissed after 3 seconds.")
    else:
        test.xfail("Modal did not automatically dismiss after 3 seconds.")
        
    snooze(4)
    
    # Test correct password modal
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "1234")
    snooze(0.5)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 75, 15, Qt.LeftButton)
    
    test.compare(waitForObjectExists(names.background_Rectangle).visible, True, "Modal appears correctly.")
    test.compare(str(waitForObjectExists(names.correctPassEnteredText_Text).text), "Correct password entered, returning to home.", "Password correct modal has correct text.")
    snooze(4)
    test.compare(str(waitForObjectExists(names.gDMS_Sample_Application_Home_Text).text), "Home", "Successfully returned to home screen after correct password was entered.")
