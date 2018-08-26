Feature: Log into Trello

  Scenario: Registered user can log in to Trello
     Given The trello.com is opened
       And The login page is opened
      When In login form email "rafal.zajac.t@gmail.com" and password "testautomatyczny" are entered
      Then User is logged in