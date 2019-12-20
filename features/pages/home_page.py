from selenium.webdriver.common.by import By
from features.pages.base_page_object import BasePage


class HomePage(BasePage):

    locator_dictionary = {
        "login_button": (By.XPATH, "(//button[@class='display-flex flex-items-xs-middle flex-items-xs-center bt'])[1]")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def clickLoginButton(self):
        self.find_element(self.locator_dictionary['login_button']).click()
