# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appsampleApp")
    # attachToApplication("appsampleApp")
    
    setWindowState(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), WindowState.Maximize)
    snooze(1)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 43, 47, Qt.LeftButton)  
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text).text), "John Doe",
        "Compare callerName text property to expected value.")
    test.compare(str(waitForObjectExists(names.phoneDelegate_111_111_1111_Text).text), "111-111-1111",
        "Compare phoneNumber text property to expected value.")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle).callDuration, 0,
        "Compare callDuration custom property to expected value.")    
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_111_111_1111_Text).text), "111-111-1111")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_2).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_222_222_2222_Text).text), "222-222-2222")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_2).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_3).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_333_333_3333_Text).text), "333-333-3333")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_3).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_4).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_444_444_4444_Text).text), "444-444-4444")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_4).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_5).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_555_555_5555_Text).text), "555-555-5555")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_5).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_6).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_666_666_6666_Text).text), "666-666-6666")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_6).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_7).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_777_777_7777_Text).text), "777-777-7777")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_7).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_8).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_888_888_8888_Text).text), "888-888-8888")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_2).callDuration, 0)
    
    test.compare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_9).text), "John Doe")
    test.compare(str(waitForObjectExists(names.phoneDelegate_999_999_9999_Text).text), "999-999-9999")
    test.compare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_2).callDuration, 0)
    
    test.xcompare(str(waitForObjectExists(names.phoneDelegate_John_Doe_Text_10).text), "John Do")
    test.xcompare(str(waitForObjectExists(names.phoneDelegate_000_000_0000_Text).text), "000-000-000")
    test.xcompare(waitForObjectExists(names.phoneView_phoneDelegate_Rectangle_10).callDuration, 1)
