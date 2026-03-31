from selenium.webdriver.support.wait import WebDriverWait
from utils.element_actions import ElementActions


class BasePage:
    TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser
        self.driver = browser
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)
        self.actions = ElementActions(browser)
