from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ElementActions:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.TIMEOUT)

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

    def get_text_from_elements(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [el.text.strip() for el in elements if el.text.strip()]
