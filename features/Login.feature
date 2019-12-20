# Created by Serhii Kishchenko at 20.12.2019
Feature: Login and logout the site
  As a customer I should be able to login and log out the https://www.lotteryheroes.com/ using email = 'kishchenkos@mydigicode.com' and password = 'Q123456789'

  Scenario: Click the Login button
    When I click the Login button
    Then I check the Sign In page is opened