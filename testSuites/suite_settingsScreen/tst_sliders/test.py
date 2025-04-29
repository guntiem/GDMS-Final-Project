# -*- coding: utf-8 -*-

import names


def main():
    # startApplication("appsampleApp")
    attachToApplication("appSampleApp")
    
    #Open the settings screen 
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 58, 42, Qt.LeftButton)
   
    #Test the Volume Slider (no volume, full volume)
    mouseDrag(waitForObject(names.o_Rectangle), 5, 8, -107, -2, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.o_Rectangle), 3, 5, 164, 0, Qt.NoModifier, Qt.LeftButton)
    test.passes("Volume Slider is working")
    #Test the Vertical Slider
    mouseDrag(waitForObject(names.o_Rectangle_2), 6, 9, 1, -51, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.o_Rectangle_2), 8, 9, 0, 63, Qt.NoModifier, Qt.LeftButton)
    test.passes("Ring Slider is working")
    #Test the Vertical Slider 2
    mouseDrag(waitForObject(names.o_Flickable), 190, 267, 2, 21, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.o_Rectangle_3), 1, 2, 0, 35, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.o_Rectangle_3), 1, 2, 2, -88, Qt.NoModifier, Qt.LeftButton)
    test.passes("Notification Slider is working")
    test.passes("All sliders are working, test case passed")
    
    # Remove later(?) - Tony
    mouseWheel(waitForObject(names.o_Flickable), 507, 280, 0, -180, Qt.NoModifier)
    mouseClick(waitForObject(names.back_Button), 66, 14, Qt.LeftButton)
