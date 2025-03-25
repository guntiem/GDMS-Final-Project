# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    test.imagePresent("lockedIcon", { "tolerant": True, "threshold": 89.596, "minScale": 70, "maxScale": 100, "multiscale": True }, waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl))
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 8, 18, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 13, 19, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 13, 27, Qt.LeftButton)
    test.imagePresent("lockedIcon")
