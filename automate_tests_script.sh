#!/bin/bash

test_failed=0

# Run test suite 1
'/path/to/squish-for-qt-8.0.0/bin/squishrunner' --testsuite '/path/to/suite_lockscreenTesting' --local > lockscreentestresults.txt 2>&1
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
