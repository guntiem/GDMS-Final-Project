import names
import traceback
import time

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

    # Click action
    #actual_action = "click"
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 39, 46, Qt.LeftButton)
    #compareWithLog(actual_action, "click", "gDMS_Sample_Application_RoundButton")

    # Click action
    actual_action = "click"
    mouseClick(waitForObject(names.security_Settings_Button), 62, 20, Qt.LeftButton)
    compareWithLog(actual_action, "longPress", "security_Settings_Button")

    # Double Click action
    actual_action = "doubleClick"
    doubleClick(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)
    compareWithLog(actual_action, "longPress", "security_Settings_Button")

    # Click action
    actual_action = "click"
    mouseClick(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)
    compareWithLog(actual_action, "longPress", "security_Settings_Button")


    # Long Press Action 
    actual_action = "longPress"
    mousePress(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)
    time.sleep(1.5)
    mouseRelease(waitForObject(names.security_Settings_Button), 84, 12, Qt.LeftButton)
    compareWithLog(actual_action, "longPress", "security_Settings_Button")

    # Click action to close
    mouseClick(waitForObject(names.close_Button), 34, 18, Qt.LeftButton)


if __name__ == "__main__":
    main()

