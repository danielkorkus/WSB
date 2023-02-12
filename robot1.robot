# https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
# zawsze dwie spacje od argumentu, lub [TAB]!, jednej spacji nie widzi!
*** Settings ***
Library     SeleniumLibrary

*** Variables ***



*** Keywords ***



*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org  edge
    Click Element   pt-login
    sleep           3
    Input Text      wpName1     RobotTests
    Input Text      //*[@id="wpPassword1"]  RobotFramework
