from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CHECK_BUTTON = (By.CLASS_NAME, "check")
    SCORE = (By.CLASS_NAME, "score")
    MESSAGE = (By.CLASS_NAME, "message")
    HIGHSCORE = (By.CLASS_NAME, "highscore")
    GUESS = (By.CLASS_NAME, "guess")
    NUMBER = (By.CLASS_NAME, "number")
    BACKGROUND_COLOR = (By.CSS_SELECTOR, "body")


class SearchResultsPageLocators(object):
    pass
