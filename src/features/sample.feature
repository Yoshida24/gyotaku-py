Feature: Take Gyotaku of cucumber.io TOP Page

  Scenario: Opening example.com and taking a screenshot after clicking a button
    Given I open "https://cucumber.io/"
    Then I wait for 3 seconds
    Then I click the "a[href="/docs"]"
    Then I wait for 3 seconds
    Then I save a capture to "welcome/captures"
    Then I save a HTML snapshot to "welcome/html"
    Then end
