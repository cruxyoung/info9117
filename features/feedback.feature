Feature: Send feedback

	Scenario: Send feedback
		Given I am in feedback page
		When I register with User name, Email, Subject, Message
		Then I should be shown thank message
