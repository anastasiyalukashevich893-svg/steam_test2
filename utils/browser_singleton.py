from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class BrowserSingleton:
    _instance = None
    _driver = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_driver(self, language):
        if self._driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--window-size=1920x1080")

            if language == 'russian':
                chrome_options.add_argument("--lang=ru")
                chrome_options.add_argument("--accept-lang=ru")
            else:
                chrome_options.add_argument("--lang=en")
                chrome_options.add_argument("--accept-lang=en")

            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(10)
            self._current_language = language


        elif self._current_language != language:
            self.quit_driver()
            return self.get_driver(language)

        return self._driver

    def quit_driver(self):
        if self._driver is not None:
            try:
                self._driver.quit()
            except:
                pass
            self._driver = None
            self._current_language = None
