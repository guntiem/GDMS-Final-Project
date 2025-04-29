import re
import names
from squish import *

def main():
    test.log("script actually started")  
    attachToApplication("appsampleApp")
    test.log("Navigating to Contacts")

    # Navigate to Contacts page (as before)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton),  Qt.LeftButton)
    mouseClick(waitForObject(names.tableView_Rectangle_5),               Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_tableView_TableView), Qt.LeftButton)    

    table = waitForObject(names.gDMS_Sample_Application_tableView_TableView)
    col_count = table.myColCount  
    if col_count == 4:
        test.log("Table has 4 columns as expected")
    else:
        test.fail("Table column count is not as expected. Found: " + str(col_count))
        



 
