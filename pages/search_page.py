from selenium.common import TimeoutException
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    SEARCH_RESULT = (By.ID, 'search_resultsRows')
    BUTTON_FOR_SORT = (By.ID, 'sort_by_trigger')
    HIGHEST_PRICE = (By.ID, 'Price_DESC')
    NAME_FOR_GAMES = (By.XPATH, './/div[contains(@class, "search_name ellipsis")]/span')
    PRICE = (By.XPATH, './/div[contains(@class, "discount_final_price")]')
    GAMES_LIST = (By.XPATH, '//*[@id = "search_resultsRows"]//a')
    LOADER = (By.XPATH, '//*[@id ="search_result_container"]')

    def wait_for_result(self):
        self.actions.wait_for_visibility(self.SEARCH_RESULT)
        return self

    def wait_for_loader_to_appear(self):
        try:
            self.wait.until(EC.text_to_be_present_in_element_attribute(self.LOADER, "style", "opacity"))
            return True
        except TimeoutException:
            return False

    def wait_for_loader_to_disappear(self):
        try:
            self.wait.until_not(EC.text_to_be_present_in_element_attribute(self.LOADER, "style", "opacity"))
        except TimeoutException:
            pass
        return self

    def sort_price(self):
        self.actions.click(self.BUTTON_FOR_SORT)
        self.actions.click(self.HIGHEST_PRICE)
        if self.wait_for_loader_to_appear():
            self.wait_for_loader_to_disappear()

        self.wait_for_result()
        return self

    def get_games_list(self, count):
        titles = self.actions.get_text_from_elements(self.NAME_FOR_GAMES)
        prices = self.actions.get_text_from_elements(self.PRICE)

        games = []
        for i in range(min(count, len(titles), len(prices))):
            games.append({
                'title': titles[i],
                'price': prices[i]
            })
        return games
