Feature: Validation registered email

  Scenario: User tried to register with registered email
     Given The trello.com registration page is opened
       And In registration form name "Jan Kowalski" and wrong password "test" are entered
      When Wrong email structure "jan.nowalski.pl" is entered
      Then Wrong email address error is occured
       And Email is corrected to "jan.kowalski@test.com"
       And Password is corrected to "test1234"
       And Error is occurred that email is already taken
