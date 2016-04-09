Feature: User login
    As the System Administor
    I want to users to be able to login
    so that system can identify every users
    and personalise services accordingly
    
    Scenario Outline: Existing user login
    Given at the login screen
    When an existing user submits the correct <username> and <password>
    Then the system should return "You were logged in" as the authentication status of the user
    Examples:
      | username | password  |
      | yang     | yang   |
      | 123    | 123     |
      | 111    | 111     |
      
    Scenario Outline: Existing user (wrong password)
    Given at the login screen
    When an existing user submits the correct <username> but incorrect <password>
    Then the system should return "Invalid password" as the authentication status of the user
    Examples:
      | username | password  |
      | yang     | fadf   |
      | 123    | 12sadfasdf3     |
      | 111    | 11sd1     |
      
    Scenario Outline: Unknown user
    Given at the login screen
    When an unknown user submits some <username> and <password>
    Then the system should return "Invalid username" as the authentication status of the user
    Examples:
      | username | password  |
      | yl     | fadf   |
      | 12k3    | 12sadfasdf3     |
      | 11k1    | 11sd1     |