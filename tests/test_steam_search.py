import re
from typing import List, Dict


def parse_price(price_str: str) -> float:
    price_str = price_str.strip().lower()
    free_keywords = ['бесплатно', 'free', 'free to play', '0']
    if any(word in price_str for word in free_keywords) and not any(char.isdigit() for char in price_str):
        return 0.0
    clean_str = re.sub(r'[^\d,.]', ' ', price_str).strip()
    parts = clean_str.split()
    if not parts:
        return 0.0
    final_price_raw = parts[-1]
    final_price_raw = final_price_raw.replace(',', '.')

    try:
        return float(final_price_raw)
    except ValueError:
        return 0.0


def get_prices_from_games(games: List[Dict[str, str]]) -> List[float]:
    return [parse_price(game['price']) for game in games]


class TestSteamSearch:
    def test_search_for_games(self, home_page, game_data, language):
        game_name = game_data["name"]
        required_count = game_data["count"]
        home_page.browser.get(home_page.url)
        home_page.wait_for_page_load()
        home_page.search(game_name)
        search_page = home_page.click_search_button()
        search_page.wait_for_result()
        search_page.sort_price()
        search_page.wait_for_result()
        games = search_page.get_games_list(required_count)
        prices = get_prices_from_games(games)
        expected_prices = sorted(prices, reverse=True)

        assert prices == expected_prices, (
            f"[{language}] СОРТИРОВКА НАРУШЕНА для '{game_name}'\n"
            f" Собрано игр: {len(games)} из {required_count}\n"
            f"EXPECTED (ожидалось):\n"
            f"   {expected_prices[:10]}\n"
            f"ACTUAL (получено):\n"
            f"   {prices[:10]}\n")
