# GDMS-Final-Project

<p align="center">
    <img src="readmeMedia/squishLogo.png" width="600" />
</p>

## Overview

Our Team is with GDMS for ASU Capstone Project for GUI Test Process Development. This is our final submission repository, 
where we demonstrate the testing of a demo application on a virtual machine environment and subsequently deploy and test it on 
physical boards. The project focuses on automating GUI testing using tools like Squish and Qtqml apps.

## System Requirements

To run the application and tests successfully, ensure the following environment is set up:

- **OS**: [Ubuntu 24.04](https://ubuntu.com/download/desktop)
- **Qt**: [6.7.3](https://download.qt.io/archive/qt/6.7/6.7.3/) (with QML support). See [here](https://www.qt.io/blog/qt-6.7.3-released) for details
- **Tesseract for Squish**: 4.1.1
- **Python**: 3.12
- **Squish GUI Tester**: [Squish 8.0.0](https://www.qt.io/quality-assurance/blog/squish-8.0-released#squish-eval-form)
> 💡 **Note**: Squish requires a valid license to run. See [Squish installation guide](https://www.froglogic.com/squish/) for details.

> 💡 **Note**: _tesseract-for-squish-4.1.1_ by Squish is used in this example (See [here](https://doc.qt.io/squish/ocr-and-installing-tesseract-for-squish.html) for installation guide)

## Table of Contents

1. [Environment Setup](#environment-setup)
    * Test Automation
    * Tesseract
2. [Running Tests](#running-tests)
3. [File\/Folder Descriptions](#filefolder-descriptions)
4. [Notes](#notes)
   * OCR Implementation
5. [Troubleshooting/FAQ](#troubleshootingfaq)
    * Test Run Environment Setup FAQ
    * OCR Setup FAQ
6. [Resources](#resources)

## Environment Setup

### Test Automation

1. Go to directory _</path/to/squish-for-qt-8.0.0>/bin_
2. Run: ```./squishserver --config addAttachableAUT application_name localhost:9999 in order to make the application attachable```
3. Read more about attaching tests to running applications [here](https://doc.qt.io/squish/attaching-to-running-applications.html#:~:text=In%20the%20Squish%20IDE%2C%20from,the%20Add%20Attachable%20AUT%20dialog).

> **Note**: Make sure LD_LIBRARY is set correctly as well as AUT (read troubleshooting for help setting the library path).
> **All** test scripts should include '**attachToApplication("application_name")**' instead of '**startApplication("application_name")**'.
> **All** test scripts should return to the 'home' page after finishing their test

### Tesseract

Image and text recognition in Squish uses the open-source OCR engine **Tesseract**. 
As Tesseract is the primary OCR engine for Squish and includes all the necessary engine libraries and language files, 
it became the engine of choice for this project to prototype.

> 💡 Note: Other OCR engines may be configured for use in Squish but have not been tested. 

1. Requirements 
   - Display card that allows GPU acceleration (ex. Ubuntu on Xorg, x11)
       - Check current display server: 
       ```echo $XDG_SESSION_TYPE```

2. Installation
   1. Follow tesseract installation process. Make sure to enable **Register the Tesseract installation with Squish**.
   
   <p align="center">
       <img src="readmeMedia/tesseractInstall.png" width="550" />
   </p>
   
   2. Configure Tesseract OCR engine by clicking **Edit > Preferences** to open the Preferences window. Then in the side bar, **Squish > OCR > Tesseract** to ensure installation path with Squish. 
   3. Verify with test run. 

3. Test Run
   1. Record a test case the way you normally would using the Squish GUI
   2. Find **OCR Text** under the **Verify** tab 
   3. Select automatically detected text or configure your own **Search Text** Verification

![iconTestRun.gif](readmeMedia/iconTestRun.gif)

## Running Tests

### Test Suite Automation Script

The purpose of this script is to work alongside Squish Test Center to automate the execution of test scripts. The file 'automate_test_scripts.sh' will return a 0 if all tests run successfully, and a 1 if not. 
This script uses Squishrunner to run all the test suites and generate the test reports, to be sent to the Test Center.

#### Running the automated squish test bash script

1. Start Qt app on local server:
    - Go to directory /path/to/squish-for-qt-8.0.0/bin
        - Make sure you are running the **release** version
    - Run using:
        ```./startaut --verbose --port=9999 '</path/to/sampleApp>/build/Desktop_Qt_6_7_3-Release/appsampleApp'```
2. Run the automated script:
    ```
    cd </path/to/final_application>/GDMS-Final-Project
    chmod +x automate_test_scripts.sh
    ./automate_test_scripts.sh
    ```
    > **Note**: test results are currently stored as .txt files

## File/Folder Descriptions

```
├── README.md
├── readmeMedia/
├── automate_tests_script.sh
├── sampleApp/
│   ├── Build files (CMake)
│   ├── Source code (.qml, .cpp)
│   └── assets/
└── testSuites
    ├── 
    ├── suite_contactScreenTableTest/
    │   ├── tst_/
    │   ├── tst_case1/
    │   └── tst_case_table/
    ├── suite_imageBasedTesting/
    │   ├── screenshots/
    │   ├── shared/
    │   │   ├── searchImages/
    │   ├── tst_example/
    │   ├── tst_iconRecognition/
    │   ├── tst_logging/
    │   └── tst_textRecognition/
    ├── suite_lockscreenTesting/
    │   ├── tst_lockscreen_keyboard_input/
    │   └── tst_lockscreen_modal/
    ├── suite_phoneScreen/
    │   ├── tst_findIndexOfElementContainingString/
    │   └── tst_verifyOnAndOffScreenProperties/
    └── suite_settingsScreen/
        ├── tst_doubleClick/
        ├── tst_longPress/
        └── tst_sliders/
```

**GDMS-Final-Project/**
* **README.md** – Overview and setup instructions for the project 
* **readmeMedia/** – Assets for **README.md** files for individual test suites  
* **sampleApp/**  
   * Application source code (**ContactsScreen.qml**, **HistoryScreen.qml**, **main.cpp**, **images.qrc**, etc.)  
   * Assets and images for UI elements, including OCR testing resources  
   * CMake build files (**CMakeLists.txt**)  
* **automate_tests_script.sh** – Shell script used to example automation tasks  
* **testSuites/** – Automated test suites organized by feature (Contact screen, Lock screen, etc.) with shared Python scripts and test assets like screenshots and image references
* **suite_contactScreenTableTest/** – Test suite focused on table verification points  
* **suite_imageBasedTesting/** – Test suite focused on OCR applications for secure systems. Includes templates (**tst_iconRecognition**, **tst_textRecognition**, **tst_logging**) and example file (**tst_example**)  
   * **screenshots/** – Directory for example screenshot piping in **test_example.py** file.  
   * **shared/searchImages/** – When utilizing the integrated OCR engine in Squish, referenced images to search are stored here.  
* **suite_lockscreenTesting/** – Test suite focused on user input  
* **suite_phoneScreen/** – Test suite focused on list verification  
* **suite_settingsScreen/** – Test suite focused on general GUI inputs

## Notes:

### OCR Implementation

#### Creating Test Cases

The simplest way developers can begin creating their image-based verification test suites is by getting familiar 
with Squish's APIs for image and text verification using the GUI:

1. [test.ImagePresent()](https://doc.qt.io/squish/test-imagepresent-function.html#test-imagepresent-function): Basic Squish API to search for image on current screen 
2. [test.ocrTextPresent()](https://doc.qt.io/squish/test-ocrtextpresent-function.html): Basic Squish API to scan current screen for instances of a given string

See [this page](https://doc.qt.io/squish/squish-api.html) to find a more comprehensive list of functions to use in this process.

#### Adding Images
These images will be the source of reference while creating your test cases. After adding all of your images to a relative folder in the test suite, you will be able to select these images as pre-configure images when creating test cases using Squish's recording GUI. Additionally, when utilizing the test.ImagePresent function, the image file names will pre-populate for ease of use. 

![addingImageTest.gif](readmeMedia/addingImageTest.gif)
1. Option 1: Add images to locate during test case recording:
2. Option 2: If you have .pngs or comparable files already stored in your filesystem, you can speed up the image verification process by adding those images to the shared testSuite folder in your project. 
    * For example, in this project, you would add the icons to verify in: _GDMS-Final-Project/testSuites/suite_imageBasedTesting/shared/searchImages/<image-name.png>_ and use _image-name_ in the test.imagePresent() API.

## Troubleshooting

### Test Run Environment Setup
1. Loading Squish Qt toolkit support failed: ```libQt6Widgets.so.6: cannot open shared object file: No such file or directory```
    - Run the following: 
    ```
    find / -name libQt6Qml.so.6 2>/dev/null
    export LD_LIBRARY_PATH=/path/to/Qt/6.7.3/gcc_arm64/lib:$LD_LIBRARY_PATH
    ```
   
### OCR Environment Setup

1. Error: ```Squish desktop screenshot failed error``` when trying to implement OCR Verification.
    - This issue is due to incompatible display card/server. Depending on the Ubuntu version, the default display card may be **wayland**, which is incompatible with Squish OCR functions. 

2. When attempting to verify tesseract installation using **tesseract --version**, you get the following output:
    symbol lookup error: ```tesseract: undefined symbol: _ZN9tesseract16TessPAGERendererC1EPKc```

    - This issue is caused by incompatible Leptonica and Tesseract downloads, or multiple Tesseract versions installed in the system. Clear Tesseract and all related libraries and reinstall.

3. Error: ``` Failed retrieving the engine properties: Cannot find the Leptonica library ```
    - If encountering Leptonica library issues, verify Squish path and, if applicable, change the default **lib64** folder to **lib** as listed in the tesseract download.


## Further Resources:

**Qt6 Libraries** need to be downloaded into directory for tests to run, check setup_qt6.sh

Loading Squish Qt toolkit support failed: libQt6Widgets.so.6: cannot open shared object file: No such file or directory
![LD_LIBRARY_PATH](https://github.com/user-attachments/assets/c822e3d3-af94-4177-bd4e-6c075b127638)
run: 
- find / -name libQt6Qml.so.6 2>/dev/null

* [Squish: Installing Tesseract](https://doc.qt.io/squish/ocr-and-installing-tesseract-for-squish.html)
* [Squish: Image-based-testing example](https://doc.qt.io/squish/how-to-do-image-based-testing.html)
* [Tesseract: official repository](https://github.com/tesseract-ocr/tesseract)
* [Qt: Tesseract limitations](https://qatools.knowledgebase.qt.io/squish/integrations/ocr-engines/ocr-limitations/)
* [Squish: APIs](https://doc.qt.io/squish/squish-api.html)
