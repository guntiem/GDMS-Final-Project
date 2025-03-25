# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 54, 40, Qt.LeftButton)
    test.ocrTextPresent("0123456", { "tesseract": { "psm": 3 } }, waitForObjectExists(names.gDMS_Sample_Application_QQuickWindowQmlImpl));
