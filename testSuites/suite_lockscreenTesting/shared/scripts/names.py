# encoding: UTF-8

from objectmaphelper import *

gDMS_Sample_Application_QQuickWindowQmlImpl = {"title": "GDMS Sample Application", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
gDMS_Sample_Application_RoundButton = {"checkable": False, "container": gDMS_Sample_Application_QQuickWindowQmlImpl, "type": "RoundButton", "unnamed": 1, "visible": True}
gDMS_Sample_Application_passwordField_TextField = {"container": gDMS_Sample_Application_QQuickWindowQmlImpl, "echoMode": 0, "id": "passwordField", "type": "TextField", "unnamed": 1, "visible": True}
gDMS_Sample_Application_Unlock_Phone_Button = {"checkable": False, "container": gDMS_Sample_Application_QQuickWindowQmlImpl, "id": "checkPasswordButton", "text": "Unlock Phone", "type": "Button", "unnamed": 1, "visible": True}
gDMS_Sample_Application_Home_Text = {"container": gDMS_Sample_Application_QQuickWindowQmlImpl, "text": "Home", "type": "Text", "unnamed": 1, "visible": True}
gDMS_Sample_Application_Screen_is_locked_Text = {"container": gDMS_Sample_Application_QQuickWindowQmlImpl, "text": "Screen is locked.", "type": "Text", "unnamed": 1, "visible": True}
gDMS_Sample_Application_Overlay = {"container": gDMS_Sample_Application_QQuickWindowQmlImpl, "type": "Overlay", "unnamed": 1, "visible": True}
o_Rectangle = {"color": "#0d0d0d", "container": gDMS_Sample_Application_Overlay, "type": "Rectangle", "unnamed": 1, "visible": True}
background_Rectangle = {"container": gDMS_Sample_Application_Overlay, "id": "background", "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
incorrect_password_Text = {"container": gDMS_Sample_Application_Overlay, "text": "Incorrect password.", "type": "Text", "unnamed": 1, "visible": True}
correctPassEnteredText_Text = {"container": gDMS_Sample_Application_Overlay, "objectName": "correctPassEnteredText", "type": "Text", "visible": True}
incorrectPassEnteredText_Text = {"container": gDMS_Sample_Application_Overlay, "objectName": "incorrectPassEnteredText", "type": "Text", "visible": True}
oK_Button = {"checkable": False, "container": gDMS_Sample_Application_Overlay, "text": "OK", "type": "Button", "unnamed": 1, "visible": True}
