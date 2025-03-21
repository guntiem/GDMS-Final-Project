Feature: Testing menu icon visibility

    This test goes over the scenario in which all available menu icons are visible

    Scenario: All icons are visible

        Given the application is running
          And user is in the OCRMenuTesting page
         When the muted checkbox is enabled
         Then the muted icon is visible on the top right of the screen

