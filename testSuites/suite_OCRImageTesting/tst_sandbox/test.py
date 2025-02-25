# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 25, 57, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 15, 12, Qt.LeftButton)
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
