# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 42, 38, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Image, 1858465), 519, 354, Qt.LeftButton)
