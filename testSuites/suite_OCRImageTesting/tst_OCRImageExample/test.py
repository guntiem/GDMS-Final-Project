# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 47, 37, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 11, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 15, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 10, 8, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 17, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 16, 23, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 16, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 16, 14, Qt.LeftButton)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), -19, 151)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), 8, -2)
    test.imagePresent("full_menu", {}, waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
