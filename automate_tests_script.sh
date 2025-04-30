#!/bin/bash

pass_or_fail=0

for suite_path in testSuites/suite_*/; do
    suite_name=$(basename "$suite_path")
    squishrunner --testsuite "testSuites/$suite_name" --exitCodeOnFail 1 --reportgen xml3.4,"testResults/${suite_name}Results/"
    
    if [ $? -eq 0 ]; then
        echo "${suite_name} executed successfully."
    else
        echo "${suite_name} failed."
        pass_or_fail=1
    fi

    zip -r "testResults/${suite_name}Results.zip" "testResults/${suite_name}Results/"  
    testcentercmd --url=http://$TESTCENTER_ADDRESS --token=49_337cZ7PCLY37SmciZAUR9-7fK4tQVFLhGP-0ssmM upload sampleApp "testResults/${suite_name}Results.zip"    
done   
  
if [ $pass_or_fail -eq 0 ]; then
    echo "All test suites passed!"
else
    echo "One or more test suites failed."
fi

exit $pass_or_fail
