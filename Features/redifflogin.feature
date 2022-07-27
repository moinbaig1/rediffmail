Feature: Rediff invalid Login
    Scenario: Invalid Login page for rediffmail
    Given Launch Chrome browser
    When open rediffmail login page
    Then Enter username "baig.moin" invalid password "pwd"
    And submit
    And display not valid