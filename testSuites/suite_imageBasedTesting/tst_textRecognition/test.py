# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    > test.ocrTextPresent(): test for visual text recognition.  Ref: https://doc.qt.io/squish/test-ocrtextpresent-function.html
        - returns bool: True when first argument passed (text to test value) is recognized in search region
        > arguments: (text, [parameterMap], [searchRegion])
            - parameterMap: {'tesseract': ('parameter' : 'value', ...}}
                - parameters: interval(ms), timeout(ms) occurence, profiles, options, scalefactor, message
                - tesseract parameters: mode, psm, preprocessing
            - searchRegion: 
                - empty value (default) searches entire physical display
                - reduce screen area by object to reduce visual noise -> increase OCR validity (https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
                - Ref: https://doc.qt.io/squish/improving-object-identification.html
            
    > OCR tuning:
        - image processing
        > noisy text handling: use "mdoe" parameter. LSTM ("mode": "1") is used in this example.
        > page segmentation modes ("psm"): https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/
            - used in this example file:
                - 3: Fully Automatic Page Segmentation, But No OSD (best performance)
                - 11: Sparse Text: Find as Much Text as Possible in No Particular Order
              
    
'''

import names
    
SCREEN = names.gDMS_Sample_Application_QQuickWindowQmlImpl

def main():    
    global SCREEN
    #=== APPLICATION GUI INTERACTION SETUP =========================================================================================
    startApplication("appsampleApp")
    
    # entering relevant App page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    #=============================================================================================================================
    
    
    #=== BASIC TEXT PRESENT/NOT PRESENT TESTING  ======================================================================
    # this approach utilizes the entire app window screen to check for icon presence
    test.ocrTextPresent("This is Filler text to use to test the OCR engine's text", 
                        { "tesseract": { "psm": 3 } }, waitForObjectExists(SCREEN));
    test.ocrTextPresent("FiFLFFIFFl", { "tesseract": { "mode": 1, "psm": 11 } });
    
    #===============================================================================================================================
    
    
    #=== TESTING SPECIFIC WINDOW REGION (ALL PASS) =================================================================================
    # Specify by Ratio: This approach utilizes the entire window screen to check for icon presence
    BOUNDS = object.globalBounds(waitForObject(SCREEN))
    BOUNDS.width = BOUNDS.width / 2
    test.imageNotPresent('mutedIcon', {}, BOUNDS) # Will check the 2nd and 3rd quadrants
    
    # Specify by Pixels: using UiTypes.ScreenRectangle(x, y, width, height)
    # NOTE: The display screen size for this test case is 850x480
    test.imagePresent('mutedIcon', {'tolerant': False}, UiTypes.ScreenRectangle(630, 0, 220, 40)) # Only the area of the screen if max(iconsPresent)
    #===============================================================================================================================
    
    
    #=== TESTING SPECIFIC OBJECT BOUNDS (ALL PASS) =================================================================================
    # The following will grab region spanned by QtApp objects
    test.imagePresent("mutedIcon", {}, waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem))
    
    # NOTE: You can also list multiple objects, pass as a list. 
    test.imagePresent("mutedIcon", {}, [waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting_ContentItem), 
                                        waitForObjectExists(names.gDMS_Sample_Application_OCRMenuTesting)])
    #===============================================================================================================================
    
    
    
    
    

    
    

