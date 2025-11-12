*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  juho  juhonen123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kallenen123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ja  janipetteri8
    Output Should Contain  Username ja is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  jani8  janikuusi3
    Output Should Contain  Username jani8 is invalid

Register With Valid Username And Too Short Password
    Input Credentials  jimi  ab
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jimi  abcdefgh
    Output Should Contain  Password contains only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123