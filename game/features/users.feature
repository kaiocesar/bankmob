Feature: Users

    Scenario: A user can log into the app

        Given I empty the "user" table

        And I create the following users:
            | id | email               | username  | password  |
            | 1  | fulaninho@gmail.com | Fulaninho | 123123123 |

        When I log in with username "Fulaninho" and password "123123123"

        Then I am logged in