
Feature: One Debit CCD ()

  Scenario Outline: Program will successfully warn the user if Required fields are not valid.
    Given I open the login page
    When I enter the username
    And I enter the password
    And Click the login button
    And I open the Debit CCD Form
    And I add a company name
    And fills in a "<routing_number>" and a "<first_name>" and a "<last_name>"
    And fills a "<dl_State>" and a "<dl_number>" and a "<account_number>"
    And fills a "<check_amount>" and a "<require_Address>"
    And fills additional required fields
    And Submits the Form
    Then I will check "<response>"
    And I close the browser

    Examples:
    Data Table Deleted

