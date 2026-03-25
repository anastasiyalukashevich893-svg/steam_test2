from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    SEARCH_RESULT = (By.ID, 'search_resultsRows')
    BUTTON_FOR_SORT = (By.ID, 'sort_by_trigger')
    HIGHEST_PRICE = (By.ID, 'Price_DESC')
    NAME_FOR_GAMES = (By.XPATH, './/div[contains(@class, "search_name ellipsis")]/span')
    PRICE = (By.XPATH, './/div[contains(@class, "discount_final_price")]')
    GAMES_LIST = (By.XPATH, '//div[@id = "search_resultsRows"]//a')

    def __init__(self, browser):
        super().__init__(browser)

    def wait_for_result(self):  # ждем когда загрузятся результаты
        self.wait_for_visibility(self.SEARCH_RESULT)
        return self

    def sort_price(self):
        self.click(self.BUTTON_FOR_SORT)
        self.click(self.HIGHEST_PRICE)
        old_results = self.find_all(self.SEARCH_RESULT)
        if old_results:
            self.wait.until(EC.staleness_of(old_results[0]))

        self.wait_for_result()
        return self

    def get_games_list(self, count):
        games = []
        self.wait_for_result()
        game_blocks = self.find_all(self.GAMES_LIST)

        for block in game_blocks[:count]:
            titles = block.find_elements(*self.NAME_FOR_GAMES)
            prices = block.find_elements(*self.PRICE)

            if titles and prices:
                title = titles[0].text.strip()
                price = prices[0].text.strip()
                games.append({'title': title, 'price': price})
                print(f"   {len(games)}. {title[:50]}... - {price}")

        return games

    @staticmethod
    def verify_sorting(games):
        prices = []
        for game in games:
            price_str = game['price'].replace('₽', '').replace('$', '').replace(' ', '').strip()

            if price_str in ['бесплатно', 'Free', '']:
                prices.append(0)
            elif price_str.replace('.', '').isdigit():
                prices.append(float(price_str))
            else:
                prices.append(0)

        return prices == sorted(prices, reverse=True)
