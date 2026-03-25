import pytest
from utils.browser_singleton import BrowserSingleton
from pages.home_page import HomePage
from data.test_data import TestData


@pytest.fixture(params=TestData.LANGUAGE)
def language(request):
    return request.param


@pytest.fixture
def browser(language):
    browser_singleton = BrowserSingleton()
    driver = browser_singleton.get_driver(language)
    yield driver
    browser_singleton.quit_driver()


@pytest.fixture
def home_page(browser):
    return HomePage(browser)


@pytest.fixture(params=TestData.GAMES)
def game_data(request):
    return request.param