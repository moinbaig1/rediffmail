Feature: Rediff valid Login
    Scenario: Valid Login page for rediffmail
    Given Launch Chrome browser
    When open rediffmail login page
    Then Enter username "baig.moin" valid password "Fuzail_1988"
    And submit
    And display valid