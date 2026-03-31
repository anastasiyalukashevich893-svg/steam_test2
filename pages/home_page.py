from pages.base_page import BasePage
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from utils.element_actions import ElementActions


class HomePage(BasePage):
    URL = 'https://store.steampowered.com/'
    PAGE_OVERLAY = (By.XPATH, '//div[contains(@class, "carousel_container maincap")]')
    MAINE_PAGE = (By.ID, "home_featured_and_recommended")
    SEARCH_THE_STORE = (By.XPATH, "//input[@name='term']")
    SEARCH_BUTTON = (By.XPATH, "//form[@role='search']/button")

    def __init__(self, browser):
        super().__init__(browser)

    def wait_for_page_load(self):
        self.actions.wait_for_visibility(self.PAGE_OVERLAY)
        return self

    def search(self, game_name):
        self.actions.send_keys(self.SEARCH_THE_STORE, game_name)
        return self

    def click_search_button(self):
        self.actions.click(self.SEARCH_BUTTON)
        return SearchPage(self.browser)
