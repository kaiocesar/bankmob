Feature: Add up numbers

As a mathematically challenged user
I Want to add numbers
So that I know the total

Scenario: Add two numbers
    Given I have entered 50 into the calcular
    And I have entered 30 into the calculator
    When I press add
    Then the result should be 80 on the screen