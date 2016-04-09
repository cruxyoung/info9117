Feature: User register
    As the system administor
    so that system remember the usernames and passwords of users
    and do not allow user to use the username which has been used
    and check the password in case the username inputed by user is not what they want
    
    
    Scenario Outline: New user register
        Given at the register screen
        When an new user submits the <username> and <password> and same <password2>
        Then the system should return "You were successfully registered and can login now"
        Examples:
        | username | password  |password2|
        | yn       | yang      |yang     |
        | 1k2      | 123       |123      |
        | 11j      | 111       |111      |
        
    

    Scenario Outline: New user register
        Given at the register screen
        When an new user submits the <username> and <password> and not same <password2>
        Then the system should return "The two passwords do not match"
        Examples:
        | username | password  |password2|
        | yns       | yang      |yag     |
        | 1k2d      | 123       |12      |
        | 11fj      | 111       |11      |
        

    Scenario Outline: New user register
        Given at the register screen
        When an new user submits the same <username> and <password> and <password2>
        Then the system should return "The username is already taken"
        Examples:
        | username | password  |password2|
        | yang       | yang      |yang     |
        | 123      | 123       |123      |
        | 111      | 111       |111      |















    