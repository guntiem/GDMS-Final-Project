#!/bin/bash

test_failed=0
squishrunner_path='/home/vboxuser/squish-for-qt-8.1.0/bin/squishrunner'
testsuites_path='/home/vboxuser/GDMS-Final-Project/testSuites'
testcenter_path='/home/vboxuser/testcenter-4.1.1-linux-x64/'

#--local > 'test_results/lockscreentestresults.txt' 2>&1

"$squishrunner_path" --testsuite "$testsuites_path/suite_lockscreenTesting" --reportgen xml.3.4,test_reports/
if [ $? -ne 0 ]; then
    echo "Test suite 1 failed."
    test_failed=1
else
    echo "Test suite 1 executed successfully."
fi

#"$testcenter_path/bin/testcentercmd" --url=http://localhost:8800 --token=49_337cZ7PCLY37SmciZAUR9-7fK4tQVFLhGP-0ssmM upload sampleApp 'test_results/lockscreentestresults.txt'


if [ $test_failed -ne 0 ]; then
    echo "One or more test suites failed."
else
    echo "All test suites passed!"
fi

exit $test_failed 
