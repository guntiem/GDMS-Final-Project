# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appsampleApp")
    
    # Navigate to phone call screen
    setWindowState(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), WindowState.Maximize)
    snooze(1)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 40, 42, Qt.LeftButton)
    
    # End every call in the list view
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.phoneDelegate_End_Button), 68, 47, Qt.LeftButton)
    
    test.compare(waitForObjectExists(names.gDMS_Sample_Application_phoneView_ListView).count, 0, 
        "Confirm that list view count is 0 after ending all calls.")
    
    snooze(5)
    
    # Dynamically add new calls
    doubleClick(waitForObject(names.gDMS_Sample_Application_Call_Button), 129, 26, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Call_Button), 129, 26, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_1_Button), 68, 47, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_2_ABC_Button), 43, 41, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_3_DEF_Button), 25, 29, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_4_GHI_Button), 61, 41, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_5_JKL_Button), 60, 36, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_6_MNO_Button), 49, 33, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_7_PQRS_Button), 44, 32, Qt.LeftButton)
    mouseDrag(waitForObject(names.numberPad_8_TUV_Button), 40, 29, 0, 0, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_9_WXYZ_Button), 33, 37, Qt.LeftButton)
    mouseClick(waitForObject(names.numberPad_0_Button), 32, 36, Qt.LeftButton)  
    doubleClick(waitForObject(names.gDMS_Sample_Application_Call_Button), 171, 29, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Call_Button), 167, 27, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Call_Button), 167, 27, Qt.LeftButton)
    
    phone_numbers = []
    
    for i in range(waitForObject(names.gDMS_Sample_Application_phoneView_ListView).count):
        #delegate = waitForObject({"container": names.gDMS_Sample_Application_phoneView_ListView, "id": "phoneDelegate", "index": i, "type": "Rectangle", "unnamed": 1, "visible": True})
        #inner_rect = waitForObject({"container": {"container": names.gDMS_Sample_Application_phoneView_ListView, "id": "phoneDelegate", "index": i, "type": "Rectangle", "unnamed": 1, "visible": True}, "id": "innerRect", "type": "Rectangle", "unnamed": 1, "visible": True})
        phone_number = str(waitForObject({"container": {"container": {"container": names.gDMS_Sample_Application_phoneView_ListView, "id": "phoneDelegate", "index": i, "type": "Rectangle", "unnamed": 1, "visible": True}, "id": "innerRect", "type": "Rectangle", "unnamed": 1, "visible": True}, "id": "phoneNumber", "type": "Text", "visible": True}).text)
        if phone_number == "":
            continue
        phone_numbers.append(phone_number)
    
    test.compare(phone_numbers, ["1234567890"], "Confirm that list index of specific phone number was able to be found.")    
