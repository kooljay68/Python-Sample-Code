
  Feature: Check All Reports

  Scenario Outline: Test Virtual Terminal Gift - GiftCard
    Given I open the login page
    When I enter the username
    And I enter the password
    And Click the login button
    And I open the Reports Tab
    And I print the report test "<report_name>"
    And I select the report by "<report_name>"
    And I enter the transactions "<from1>" and "<from_true>" and "<test_type>"
    And I enter the transactions to "<to>" and "<to_true>" and "<test_type>"
    And I select the filter "<filter_type>" and "<filter_true>" and "<test_type>"
    And I enter a clerk ID "<clerk_id>" and "<clerk_id_true>" and "<test_type>"
    Then I click view report
    And I Check the "<response>"
    And I close the browser

  Examples:
    |report_name                                     |from1    |from_true   |to       |to_true    |clerk_id   |clerk_id_true    |response         |filter_type |filter_true |test_type |
  Data Table Deleted
