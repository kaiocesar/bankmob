Feature: Users

    Background: A user can log into the app

        Given I empty the "user" table

        And I create the following users:
            | id | email               | username  | password  |
            | 1  | fulaninho@gmail.com | Fulaninho | 123123123 |

        When I log in with username "Fulaninho" and password "123123123"

        Then I am logged in


    Scenario: A user can see a list of friends

        Given I empty the "Friendship" table

        And I create the following friendships:
            | id | user1 | user2 |
            | 1  | 1     |  2    |

        When I get a list of friends

        Then I see the following response data:
            | id | email               | username  |
            | 2  | fulaninho@gmail.com | Fulaninho |