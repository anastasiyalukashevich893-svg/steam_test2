from utils.config import ConfigReader


class TestData:
    LANGUAGES = ConfigReader.get_config().language
    GAMES = [{"name": "The Witcher", "count": 10},
             {"name": "Fallout", "count": 20}]
