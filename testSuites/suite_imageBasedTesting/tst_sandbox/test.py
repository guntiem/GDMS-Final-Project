# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 39, 35, Qt.LeftButton)
    test.ocrTextPresent("UPPERCASE", { "tesseract": { "psm": 3 } });
