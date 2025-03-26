# -*- coding: utf-8 -*-
''' TEMPLATE NOTES:
    > test.ocrTextPresent(): test for visual text recognition.  Ref: https://doc.qt.io/squish/test-ocrtextpresent-function.html
        - returns bool: True when first argument passed (text to test value) is recognized in search region
        > arguments: (text, [parameterMap], [searchRegion])
            - parameterMap: {'tesseract': ('parameter' : 'value', ...}}
                - parameters: interval(ms), timeout(ms) occurrence, profiles, options, scalefactor, message
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
TEXT_SECTION = names.gDMS_Sample_Application_This_is_filler_text_to_use_to_test_the_OCR_engine_s_text_verification_UPPERCASE_lowercase_MiXeD_cAsE_01234_Full_width_numbers_Special_characters_Il1_O0Q_Similar_looking_characters_Ligatures_Text
    

def main():    
    global SCREEN, TEXT_SECTION
    #=== APPLICATION GUI INTERACTION SETUP =========================================================================================
    startApplication("appsampleApp")
    
    # entering relevant App page...
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 46, 50, Qt.LeftButton)
    #=============================================================================================================================
    
    
    #=== BASIC TEXT PRESENT/NOT PRESENT TESTING ======================================================================
    # this approach utilizes the entire app window screen to check for icon presence
    test.ocrTextPresent("This is Filler text to use to test the OCR engine's text", 
                        { "tesseract": { "psm": 3 } }, waitForObjectExists(SCREEN));
                        
    test.ocrTextPresent("FiFLFFIFFl", { "tesseract": { "mode": 1, "psm": 11 } });
    
    #===============================================================================================================================

    
    #=== LOWER/UPPER CASES =================================================================================
    test.ocrTextPresent("CASE", { "tesseract": { "psm": 3 }, "occurrence": 2 }, waitForObjectExists(TEXT_SECTION));
    
    test.ocrTextPresent("UPPERCASE", {"message":"Expected UPPERCASE"})
    test.ocrTextPresent("lowercase", {"message":"Expected lowercase"})
    test.ocrTextPresent("MiXeD cAsE", {"message":"Expected MiXeD cAsE"})
    
    test.ocrTextPresent("mixed case", {"message":"Checking to see if letter case blocks test failure"})
    #===============================================================================================================================
    
    
    #=== NUMBERS AND SPACING =================================================================================
    #checking for concurrent digits
    test.ocrTextPresent("01234", {"message": "Expected regular digits 0-9."})
    test.ocrTextPresent("56789", {"message": "Expected Full-Width digits 0-9."})
    
    #testing for individual digits
    test.ocrTextPresent("1")
    test.ocrTextPresent("2")
    test.ocrTextPresent("3")
    
    test.ocrTextPresent("0123456789", {"message": "Testing full 0123456789 (regular-full mix)."})
    #===============================================================================================================================
    
    
    #=== SPECIAL CHARACTERS =================================================================================
    # full character recognition testing...
    test.ocrTextPresent("!@#$%^&*()_+-=[]{}|;:'\",.<>?/", {"message": "Expected all characters to match"})
    #===============================================================================================================================
    
    
    #=== SIMILAR CHARACTERS =================================================================================
    test.ocrTextPresent("Il1| O0Q", {"message":"Expected value: Il1| O0Q"})
    #===============================================================================================================================
    
    
    #=== LIGATURES =================================================================================
    
    #===============================================================================================================================
    
    closeWindow(names.gDMS_Sample_Application_QQuickWindowQmlImpl)
    
    
    

    
    

