
  Feature: Check All Reports

  Scenario Outline: ET-737 Test Virtual Terminal Gift - GiftCard
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
    |Gift & Loyalty Store Reconciliation             |01012016 |true        |10012018 |true       |001        |false            |Records: 2       |Default     |false       |0         |
    |Gift & Loyalty Aging/Expiration Report          |01012016 |false       |10012018 |false      |001        |false            |Records: 220     |Default     |false       |0         |
    |Discount Provided Summary                       |01012016 |true        |10012018 |true       |001        |false            |Records: 2       |Default     |false       |0         |
    |Discount Provided Detail                        |01012016 |true        |10012018 |true       |001        |false            |Records: 2       |Default     |false       |0         |
    |Shop Local Reconciliation Details               |01012016 |true        |10012018 |true       |001        |false            |Records: 0       |Default     |false       |1         |
    |Shop Local Reconciliation Summary               |01012016 |true        |10012018 |true       |001        |false            |Records: 0       |Default     |false       |1         |
    |Loyalty Transaction Points Detail               |01012016 |true        |10012018 |true       |001        |false            |Records: 62      |Default     |false       |2         |
    |Loyalty Transaction Points Summary              |01012016 |true        |10012018 |true       |001        |false            |Records: 24      |Default     |false       |2         |
    |Loyalty Transaction Points Averages             |01012016 |true        |10012018 |true       |001        |false            |Records: 24      |Default     |false       |2         |
    |Gift & Loyalty Customer Registration            |01012016 |false       |10012018 |false      |001        |false            |Records: 16      |Default     |false       |0         |
    |Gift & Loyalty Clerk Transaction Detail         |01012016 |true        |10012018 |true       |001        |true             |Records: 249     |Default     |false       |3         |
    |Gift & Loyalty Clerk Transaction Summary        |01012016 |true        |10012018 |true       |001        |true             |Records: 70      |Default     |false       |3         |
    |Gift & Loyalty Transaction Detail               |01012016 |true        |10012018 |true       |001        |false            |Records: 474     |Default     |false       |2         |
    |Gift & Loyalty Transaction Summary              |01012016 |true        |10012018 |true       |001        |false            |Records: 76      |Default     |false       |2         |
    |Gift & Loyalty Transaction Averages             |01012016 |true        |10012018 |true       |001        |false            |Records: 76      |Default     |false       |2         |
