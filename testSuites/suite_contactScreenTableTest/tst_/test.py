import re
import names
from squish import *

def main():
    test.log("script actually started")  
    startApplication("appsampleApp")
    test.log("Navigating to Contacts")

    # Navigate to Contacts page (as before)
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton),  Qt.LeftButton)
    mouseClick(waitForObject(names.tableView_Rectangle_5),               Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_tableView_TableView), Qt.LeftButton)

    # Verify the phone number format (as before)
        
    jane_email = str(waitForObjectExists(names.jane_smith_example_com_Text).text)
    email_pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    if email_pattern.fullmatch(jane_email):
        test.log(f"Jane's email is valid: {jane_email}")
    else:
        test.fail(f"Invalid email format: {jane_email}")

        
        

    
    
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



 