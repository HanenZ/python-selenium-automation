Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input python into search field
    And Click on search icon
    Then Product results for python are shown