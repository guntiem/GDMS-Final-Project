# -*- coding: utf-8 -*-

import names


def main():
    startApplication("appsampleApp")
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 12, 37, Qt.LeftButton)
    test.imagePresent("alertIcon")
    doubleClick(waitForObject(names.gDMS_Sample_Application_This_is_filler_text_to_use_to_test_the_OCR_engine_s_text_verification_UPPERCASE_lowercase_MiXeD_cAsE_01234_Full_width_numbers_Special_characters_Il1_O0Q_Similar_looking_characters_Ligatures_Text))
