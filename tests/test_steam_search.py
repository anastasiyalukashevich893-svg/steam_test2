

class TestSteamSearch:
    def test_search_for_games(self, home_page, game_data, language):
        game_name = game_data["name"]
        required_count = game_data["count"]
        home_page.open_home_page().wait_for_page_load()
        assert home_page.is_element_present(home_page.PAGE_OVERLAY), 'Главная страница не открылась'
        home_page.search(game_name)
        search_page= home_page.click_search_button()
        search_page.wait_for_result()
        assert search_page.is_element_present(search_page.SEARCH_RESULT), "Страница поиска не загружена"
        search_page.sort_price()
        search_page.wait_for_result()
        games = search_page.get_games_list(required_count)
        assert search_page.verify_sorting(games), "Игры не отсортированы по убыванию цены"



