#!/bin/bash

test_failed=0

# Run test suite 1
'/home/tony/squish-for-qt-8.0.0/bin/squishrunner' --testsuite '/home/tony/Desktop/final_application/GDMS-Final-Project/testSuites/suite_lockscreenTesting' --local > lockscreentestresults.txt 2>&1
if [ $? -ne 0 ]; then
    echo "Test suite 1 failed."
    test_failed=1
else
    echo "Test suite 1 executed successfully."
fi





if [ $test_failed -ne 0 ]; then
    echo "One or more test suites failed."
else
    echo "All test suites passed!"
fi

exit $test_failed
