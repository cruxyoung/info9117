Feature: User register
    As the system administor
    so that system remember the usernames and passwords of users
    and do not allow user to use the username which has been used
    and check the password in case the username inputed by user is not what they want
    
    
    Scenario Outline: New user register
        Given at the register screen
        When an new user submits the <username> and <password> and <password2>
        Then the system should return "You were successfully registered and can login now"
        Examples:
        | username | password  |password2|
        | yang     | yang   |yang|
        | 123    | 123     |123|
        | 111    | 111     |111|