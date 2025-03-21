# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_Image), 803, 314, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 67, 37, Qt.LeftButton)
    snooze(1.4)
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
