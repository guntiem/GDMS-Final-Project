import names
import traceback

# Custom compare function with error logging for action verification
def compareWithLog(actual, expected, element_name):
    try:
        if actual == expected:
            test.compare(actual, expected, f"Success: {element_name} action matches expected.")
            test.log(f"Custom success message: {element_name} performed correctly.")
        else:
            raise AssertionError(f"ERROR: {element_name} action mismatch! Detected: {actual}. Expected: {expected}.")
    except AssertionError as e:
        test.fail(f"{str(e)}\nTRACEBACK:\n{traceback.format_exc()}")

def main():
    startApplication("appsampleApp")


    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 42, 40, Qt.LeftButton)

    mouseWheel(waitForObject(names.o_Flickable), 272, 321, 0, -15, Qt.NoModifier)


    mouseWheel(waitForObject(names.o_Flickable), 272, 321, 0, -60, Qt.NoModifier)


    # Double Click Action
    actual_action = "doubleClick"
    doubleClick(waitForObject(names.o_Rectangle_3), 82, 41, Qt.LeftButton)
    compareWithLog(actual_action, "doubleClick", "o_Rectangle_3")

    # Click Actions
    actual_action = "click"
    mouseClick(waitForObject(names.o_Rectangle_4), 36, 40, Qt.LeftButton)
    compareWithLog(actual_action, "doubleClick", "o_Rectangle_4")

    mouseClick(waitForObject(names.o_Rectangle_4), 36, 40, Qt.LeftButton)
    compareWithLog(actual_action, "doubleClick", "o_Rectangle_4")

    # Flick Action
    actual_action = "flick"
    flick(waitForObject(names.o_Flickable_2), 0, 0)
    compareWithLog(actual_action, "doubleClick", "o_Flickable_2")

    # Click Action (Back Button)
    actual_action = "click"
    mouseClick(waitForObject(names.back_Button), 8, 10, Qt.LeftButton)
    compareWithLog(actual_action, "doubleClick", "back_Button")

if __name__ == "__main__":
    main()

