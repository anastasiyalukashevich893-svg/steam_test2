from pages.base_page import BasePage
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    URL = 'https://store.steampowered.com/'
    PAGE_OVERLAY = (By.XPATH, '//div[contains(@class, "page_background_overlay")]')
    MAIN_PAGE = (By.ID, "home_featured_and_recommended")
    SEARCH_THE_STORE = (By.XPATH, "//input[@name='term']")
    SEARCH_BUTTON = (By.XPATH, "//form[@role='search']/button")

    def __init__(self, browser):
        super().__init__(browser)

    def open_home_page(self):
        self.open(self.URL)
        return self

    def wait_for_page_load(self):
        self.wait_for_visibility(self.PAGE_OVERLAY)
        return self

    def search(self, game_name):
        self.send_keys(self.SEARCH_THE_STORE, game_name)
        return self

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        return SearchPage(self.browser)
