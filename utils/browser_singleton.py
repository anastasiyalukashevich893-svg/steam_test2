from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from utils.config import ConfigReader


class BrowserSingleton:
    _drivers = {}

    @classmethod
    def get_driver(cls, language: str = 'en'):
        if language not in cls._drivers:
            try:
                cls._drivers[language] = cls._create_driver(language)
            except (SessionNotCreatedException, WebDriverException) as e:
                print(f"Критическая ошибка при запуске браузера ({language}): {e}")
                raise
        return cls._drivers[language]

    @classmethod
    def _create_driver(cls, language: str):
        config = ConfigReader.get_config()
        options = Options()
        options.add_argument(config.get_window_size())

        options.add_argument(f"--lang={language}")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        driver = webdriver.Chrome(options=options)
        return driver

    @classmethod
    def quit_all_drivers(cls):
        for lang in list(cls._drivers.keys()):
            driver = cls._drivers.pop(lang)
            try:
                driver.quit()
            except WebDriverException as e:
                print(f"Ошибка WebDriver при закрытии сессии {lang}: {e.msg}")
