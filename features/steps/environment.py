from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context):
    driver_path = ChromeDriverManager().install()
    context.browser = webdriver.Chrome(driver_path)


def after_scenario(context, scenario):
    context.browser.quit()



