from dataclasses import dataclass
from typing import List


@dataclass
class BrowserConfig:
    window_width: int = 1920
    window_height: int = 1080
    language: List[str] = None

    def __post_init__(self):
        if self.language is None:
            self.language = ['en', 'ru']

    def get_window_size(self) -> str:
        return f"--window-size={self.window_width},{self.window_height}"


class ConfigReader:
    _config = None

    @classmethod
    def get_config(cls) -> BrowserConfig:
        if cls._config is None:
            cls._config = BrowserConfig()
        return cls._config

    @classmethod
    def set_config(cls, config: BrowserConfig):
        cls._config = config
