# -*- coding: utf-8 -*-

''' Notes:
    - test.ImagePresent() to to test ocr for icons/images.  Ref: https://doc.qt.io/squish/squish-api.html#findimage-function
        - ParameterMap -> {'param' : 'value', ...}
        - ParameterMap for test,imagePresent is:
        occurrence, interval, timeout, tolerant, threshold, multiscale, minScale, maxScale, message
    
    TODO:
    - Changing interface and create test case for interaction/change upon application state
    - expected icon test logging?? (verbose exporting)
'''


import names

def runApplication():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 12, 11, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 12, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 12, 6, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 13, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 17, 12, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 13, 17, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 13, 14, Qt.LeftButton)


# Sample usage of testing using saved image files from local saved directory                                                                                               # This is 
def verifyMenuIcon(icon_name):
    test.imagePresent(f'{icon_name}', {'tolerant': True, 
                                       'multiscale': True, 
                                       'threshold': 99.5})


def main():
    runApplication()
    
    verifyMenuIcon("mutedIcon")
    verifyMenuIcon("pauseIcon")
    verifyMenuIcon("videoIcon")
    verifyMenuIcon("voicemailIcon")
    verifyMenuIcon("pauseIcon")

    
    
