from behave import *
from features.pages.home_page import HomePage
from features.pages.sign_in import SignInPage

use_step_matcher("re")


@when("I click the Login button")
def step_impl(context):
    home_page = HomePage(context)
    home_page.open()
    home_page.clickLoginButton()


@then("I check the Sign In page is opened")
def step_impl(context):
    signIn_page = SignInPage(context)
    signIn_page.checkTitle()
