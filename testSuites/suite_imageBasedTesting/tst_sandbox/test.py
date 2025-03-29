# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_Image), 596, 297, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 54, 43, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Back_Button), 48, 10, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 33, 40, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Image), 92, 392, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Back_Button), 51, 7, Qt.LeftButton)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl, 41577), -137, -45)
    snooze(277.5)
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
