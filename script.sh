#!/bin/bash




# Run test suite 2
echo "Running settings suite"
/home/egunti/squish-for-qt-8.0.0/bin/squishrunner --testsuite '/home/egunti/GDMS-Final-Project/suite_settingsScreen' --local > SettingsSuiteResults.txt 2>&1

if [ $? -ne 0 ]; then
    echo "Test suite 2 failed."
    kill $APP_PID
    exit 1
fi

echo "Test suite 2 executed successfully."

echo "Ending Qt app..."
#kill $APP_PID
