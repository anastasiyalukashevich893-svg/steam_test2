from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser
        self.driver = browser
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return self

    def is_element_present(self, locator):
        return self.find(locator)
