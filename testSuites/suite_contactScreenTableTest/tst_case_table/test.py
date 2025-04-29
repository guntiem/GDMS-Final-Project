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

    # Verify the phone number format (as before)
    phone_number = str(waitForObjectExists(names.o123_456_7890_Text).text)
    phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if phone_pattern.fullmatch(phone_number):
        test.log("Phone number format is correct")
    else:
        test.fail("Phone number format is incorrect: " + phone_number)


    
    
    '''
    # New test: Verify that the table has 3 columns.
    table = waitForObject(names.gDMS_Sample_Application_tableView_TableView)
    model = table.model
    rows = model.rows
    '''
    
    '''
    col_count = table.myColCount  # Access the property forwarded from the model
    if col_count == 4:
        test.log("Table has 4 columns as expected")
    else:
        test.fail("Table column count is not as expected. Found: " + str(col_count))
        
    '''



 
