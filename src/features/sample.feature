Feature: Take Gyotaku of cucumber.io TOP Page

  Scenario: Opening example.com and taking a screenshot after clicking a button
    Given I open "https://cucumber.io/"
    Then I wait for 3 seconds
    Then I click the ".btn[href="/docs/installation/"]"
    Then I wait for 3 seconds
    Then I save a capture to "welcome/captures"
    Then I save a HTML snapshot to "welcome/html"
    Then end
