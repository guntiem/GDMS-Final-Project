# -*- coding: utf-8 -*-

import names

def main():
    # Start the application
    startApplication("appsampleApp")
    # attachToApplication("appSampleApp")
    
    # Click on the settings screen
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 48, 30, Qt.LeftButton)
    
    # Scroll
    mouseWheel(waitForObject(names.o_Flickable), 560, 337, 0, -15, Qt.NoModifier)
    
    # Testing Theme options
    doubleClick(waitForObject(names.o_Rectangle_4), 88, 27, Qt.LeftButton)
    test.compare(str(waitForObject(names.o_Rectangle_4).property("color")), "#0000ff", "Blue Color Selected: pass")
    
    doubleClick(waitForObject(names.green_Text))
    test.compare(str(waitForObject(names.green_Text).property("color")), "#000000", "Green Color Selected: pass")
    
    doubleClick(waitForObject(names.o_Rectangle_5), 56, 41, Qt.LeftButton)
    test.compare(str(waitForObject(names.o_Rectangle_5).property("color")), "#ffc0cb", "Pink Color Selected: pass")
    
    doubleClick(waitForObject(names.beige_Text))
    test.compare(str(waitForObject(names.beige_Text).property("color")), "#000000", "Beige Color Selected: pass")
    
    # Single click should not change the color
    mouseClick(waitForObject(names.o_Rectangle_4), 72, 28, Qt.LeftButton)
    test.compare(str(waitForObject(names.o_Rectangle_4).property("color")), "#0000ff", "Single Click: color not selected")
    
    mouseClick(waitForObject(names.green_Text))
    test.compare(str(waitForObject(names.green_Text).property("color")), "#000000", "Single Click: color not selected")
    
    mouseClick(waitForObject(names.pink_Text))
    test.compare(str(waitForObject(names.pink_Text).property("color")), "#000000", "Single Click: color not selected")
    
    test.passes("Test Case Passed: Double Click Functioning")

    # Remove later(?) - Tony
    mouseWheel(waitForObject(names.o_Flickable), 507, 280, 0, -180, Qt.NoModifier)
    # mouseClick(waitForObject(names.back_Button), 66, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.back_Button), 53, 9, Qt.LeftButton)
