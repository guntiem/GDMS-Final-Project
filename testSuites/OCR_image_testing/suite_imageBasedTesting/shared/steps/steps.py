# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names

@Given("The sample application is running")
def step(context):
    startApplication("appsampleApp")

@When("all the OCRMenu checkboxes are enabled")
def step(context):
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 36, 34, Qt.LeftButton)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), -294, -83)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Alert_CheckBox), 13, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Headphone_CheckBox), 17, 16, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Locked_CheckBox), 17, 14, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 16, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Pause_CheckBox), 18, 15, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Video_CheckBox), 16, 13, Qt.LeftButton)
    mouseClick(waitForObject(names.gDMS_Sample_Application_Voicemail_CheckBox), 10, 11, Qt.LeftButton)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), 33, 0)
    setWindowState(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), WindowState.Maximize)
    setWindowSize(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), 850, 480)
    setWindowState(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), WindowState.Normal)

@Then("all menu icons should be visible")
def step(context):
    pass

@Given("the application is running")
def step(context):
    startApplication("appsampleApp")

@Given("user is in the OCRMenuTesting page")
def step(context):
    mouseClick(waitForObject(names.gDMS_Sample_Application_RoundButton), 36, 33, Qt.LeftButton)
    moveWindow(waitForObject(names.gDMS_Sample_Application_QQuickWindowQmlImpl), -160, -42)

@When("the muted checkbox is enabled")
def step(context):
    mouseClick(waitForObject(names.gDMS_Sample_Application_Mute_CheckBox), 15, 14, Qt.LeftButton)

@Then("the muted icon is visible on the top right of the screen")
def step(context):
    test.imagePresent("mutedIcon")
