from selenium.webdriver.common.by import By

from features.pages.base_page_object import BasePage


class SignInPage(BasePage):
    locator_dictionary = {
        "title": (By.CLASS_NAME, "modal-title needsclick")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def checkTitle(self):
        assert "Sign In" in self.find_element(self.locator_dictionary['title']).text