# -*- coding: utf-8 -*-

import names


def main():
    doubleClick(waitForObject(names.gDMS_Sample_Application_Image), 570, 270, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 39, 60, Qt.LeftButton)
    snooze(1.3)
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
