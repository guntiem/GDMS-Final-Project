# -*- coding: utf-8 -*-

import names
import traceback

# Custom compare function with error logging
def compareWithLog(actual, expected, element_name):
    try:
        if actual == expected:
            test.compare(actual, expected, f"Success: {element_name} action matches expected.")
            test.log(f"Custom success message: {element_name} performed correctly.")
        else:
            raise AssertionError(f"ERROR: Mismatch for {element_name}. Expected: {expected}, but got: {actual}")
    except AssertionError as e:
        test.fail(f"{str(e)}\nTRACEBACK:\n{traceback.format_exc()}")

def main():
    startApplication("appsampleApp")

    # Click Actions
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 47, 33, Qt.LeftButton)
    mouseClick(waitForObject(names.o_Flickable), 232, 88, Qt.LeftButton)
    mouseClick(waitForObject(names.o_Flickable), 88, 73, Qt.LeftButton)
    
    mouseClick(waitForObject(names.o_Rectangle), 10, 3, Qt.LeftButton)
    mouseClick(waitForObject(names.background_SliderGroove), 2, 9, Qt.LeftButton)
    mouseClick(waitForObject(names.o_Rectangle_2), 4, 52, Qt.LeftButton)
    mouseClick(waitForObject(names.o_Flickable), 147, 159, Qt.LeftButton)
    mouseClick(waitForObject(names.background_SliderGroove_2), 1, 33, Qt.LeftButton)

    # Drag Actions
    
    mouseDrag(waitForObject(names.o_Flickable), 230, 220, -8, 71, Qt.NoModifier, Qt.LeftButton)
    compareWithLog("click", "drag", "o_Flickable")  # Expected click, but drag was performed

    mouseDrag(waitForObject(names.o_Flickable), 152, 107, -3, 73, Qt.NoModifier, Qt.LeftButton)
    compareWithLog("click", "drag", "o_Flickable")  # Expected click, but drag was performed

    mouseDrag(waitForObject(names.o_Flickable), 87, 88, 105, 9, Qt.NoModifier, Qt.LeftButton)
    compareWithLog("click", "drag", "o_Flickable")  # Expected click, but drag was performed

if __name__ == "__main__":
    main()
