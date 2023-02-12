# https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
# zawsze dwie spacje od argumentu, lub [TAB]!, jednej spacji nie widzi!
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
# ${int} , @{list} , &{str}


*** Keywords ***



*** Test Cases ***
Test 1
    #Variable       #Keywords           #Instructions
                    Open Browser        https://pl.wikipedia.org  edge
                    Click Element       pt-login
    ${my_value}     Get Text            wpName1
                    should be empty     ${my_value}
                    sleep               3
                    Input Text          wpName1     RobotTests
                    Input Text          //*[@id="wpPassword1"]  RobotFramework
