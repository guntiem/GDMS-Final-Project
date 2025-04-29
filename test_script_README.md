# Overview

The purpose of this script is to work alongside Squish Test Center to automate the execution of test scripts. The file 'automate_tests.sh' will return a 0 if all tests run successfully, and a 1 if not. 
This script uses Squishrunner to run all of the test suites and generate the test reports, to be sent to the Test Center.

# Running the automated squish test bash script

### Start Qt app on local server:

- go to directory /path/to/squish-for-qt-8.0.0/bin

- Make sure you are running the **release** version

- run using ./startaut --verbose --port=9999 '/path/to/sampleApp/build/Desktop_Qt_6_7_3-Release/appsampleApp'

### Run automated script:

- go to directory /path/to/final_application/GDMS-Final-Project

- chmod +x automate_tests_2.sh

- ./automate_tests_2.sh

- test results will be stored as .txt files


# Environment related set up

- go to directory /path/to/squish-for-qt-8.0.0/bin

run: ./squishserver --config addAttachableAUT application_name localhost:9999 in order to make the application attachable

Read more about attaching tests to running applications here: https://doc.qt.io/squish/attaching-to-running-applications.html#:~:text=In%20the%20Squish%20IDE%2C%20from,the%20Add%20Attachable%20AUT%20dialog.

Make sure LD_LIBRARY is set correctly as well as AUT (read troubleshooting for help sestting the library path)

**All** test scripts should include 'attachToApplication("application_name")' instead of 'startApplication("application_name")'

**All** test scripts should return to the 'home' page after finishing their test

# Troubleshooting:

Loading Squish Qt toolkit support failed: libQt6Widgets.so.6: cannot open shared object file: No such file or directory

run: 
- find / -name libQt6Qml.so.6 2>/dev/null

- export LD_LIBRARY_PATH=/path/to/Qt/6.7.3/gcc_arm64/lib:$LD_LIBRARY_PATH