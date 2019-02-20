
Feature: One Debit CCD ()

  Scenario Outline: ET-731 Program will successfully warn the user if Required fields are not valid.
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
      |routing_number |first_name|last_name|dl_State|dl_number    |account_number|check_amount|response               |
      |490000018      |Sam       |McHenry  |FL      |B599796600930|347548678     |1.27        |Authorization Number:  |
      |490000034      |Sam       |McHenry  |FL      |B599796600930|347548678     |1.27        |Declined               |
      |490000021      |Sam       |McHenry  |FL      |B599796600930|347548678     |1.27        |Manager Needed         |
      |490000047      |Sam       |McHenry  |FL      |B599796600930|347548678     |1.27        |Re-Presented Check     |

