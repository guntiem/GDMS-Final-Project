# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 18, 45, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Back_Button), 42, 4, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Image), 92, 408, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton_2), 44, 56, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 32, 4, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), 93, 12, Qt.LeftButton)
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "1234")
    type(waitForObject(names.gDMS_Sample_Application_passwordField_TextField), "<Return>")
    mouseClick(waitForObject(names.gDMS_Sample_Application_Unlock_Phone_Button), 32, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton_3), 50, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Back_Button), 45, 10, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton_4), 39, 22, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton_5), 77, 39, Qt.LeftButton)
    mouseWheel(waitForObject(names.phoneDelegate_Rectangle), 240, 25, 0, 60, Qt.NoModifier)
    mouseWheel(waitForObject(names.phoneDelegate_Rectangle_2), 240, 20, 0, -75, Qt.NoModifier)
    mouseClick(waitForObject(names.gDMS_Sample_Application_image_IconImage), 5, 9, Qt.LeftButton)
    snooze(1.0)
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
