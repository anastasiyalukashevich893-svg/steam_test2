import pytest
from utils.browser_singleton import BrowserSingleton
from pages.home_page import HomePage
from data.test_data import TestData


@pytest.fixture(scope="session", autouse=True)
def browser_cleanup():
    yield
    BrowserSingleton.quit_all_drivers()


@pytest.fixture(params=TestData.LANGUAGES)
def language(request):
    return request.param


@pytest.fixture
def browser(language):
    driver = BrowserSingleton.get_driver(language)
    yield driver


@pytest.fixture
def home_page(browser):
    return HomePage(browser)


@pytest.fixture(params=TestData.GAMES)
def game_data(request):
    return request.param
