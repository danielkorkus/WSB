# https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
# zawsze dwie spacje od argumentu, lub [TAB]!, jednej spacji nie widzi!
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
# ${int} , @{list} , &{str}

${error_message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
#dziala jak funkcja
Poprawne Logowanie
    #Variable       #Keywords                           #Instructions
                    Open Browser                        https://pl.wikipedia.org  edge
                    Wait Until Element Is Visible       pt-login    3   Mamy Blad!
                    Click Element                       pt-login
    ${name_value}   Get Text                            wpName1
                    should be empty                     ${name_value}
                    sleep                               3
                    Input Text                          wpName1     login
    ${pass_value}   Get Text                            //*[@id="wpPassword1"]
                    should be empty                     ${pass_value}
                    Input Text                          //*[@id="wpPassword1"]  pass
                    Checkbox Should Not Be Selected     wpRemember
                    select checkbox                     wpRemember
                    click button                        wpLoginAttempt
                    Capture Page Screenshot             screen.png
                    Close Browser


*** Test Cases ***
#   Main sub program
Test 1
    Poprawne Logowanie

Niepoprawne Logowanie
    #Variable       #Keywords                           #Instructions
                    Open Browser                        https://pl.wikipedia.org  edge
                    Wait Until Element Is Visible       pt-login    3   Mamy Blad!
                    Click Element                       pt-login
    ${name_value}   Get Text                            wpName1
                    Should Be Empty                     ${name_value}
                    Sleep                               3
                    Input Text                          wpName1     xd
    ${pass_value}   Get Text                            //*[@id="wpPassword1"]
                    Should Be Empty                     ${pass_value}
                    Log To Console                      ${pass_value}
                    Input Text                          //*[@id="wpPassword1"]  xdd
                    Checkbox Should Not Be Selected     wpRemember
                    Select Checkbox                     wpRemember
                    Click Button                        wpLoginAttempt
                    Capture Page Screenshot             screen.png
    ${my_err_msg}   Get Text                            //*[@id="userloginForm"]/form/div[1]
                    Log to Console                      ${my_err_msg}
                    Log                                 ${my_err_msg}
                    Should Be Equal As Strings          ${my_err_msg}     ${error_message}
                    Capture Page Screenshot             screen.png
                    Close Browser