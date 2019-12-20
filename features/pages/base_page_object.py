import time

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage(object):
    base_url = 'https://www.lotteryheroes.com/'

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def open(self):
        self.driver.get(self.base_url)

    # def hover(self, element):
    #     ActionChains(self.browser).move_to_element(element).perform()
    #     # I don't like this but hover is sensitive and needs some sleep time
    #     time.sleep(5)
