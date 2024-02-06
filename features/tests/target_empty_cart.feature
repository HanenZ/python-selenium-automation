# Created by zoghl at 2/6/2024
Feature: Test Scenarios for verify empty cart when opening target

  Scenario: User verify an empty cart when opening target
    Given Open target.com
    When Click on Cart icon
    Then “Your cart is empty” message is shown