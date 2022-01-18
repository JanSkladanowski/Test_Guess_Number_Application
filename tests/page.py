from locators import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys
import random


class InputValue(BasePageElement):
    locator = "guess"


class Message(BasePageElement):
    locator = "message"


class Score(BasePageElement):
    locator = "score"


class Highscore(BasePageElement):
    locator = "highscore"


class Win(BasePageElement):
    locator = "test"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    input_value = InputValue()
    message = Message()
    score = Score()
    highscore = Highscore()
    win = Win()
    starting_score = 20

    def default_conditions(self):
        default_score = self.driver.find_element(*MainPageLocators.SCORE)
        default_message = self.driver.find_element(*MainPageLocators.MESSAGE)
        default_highscore = self.driver.find_element(*MainPageLocators.HIGHSCORE)
        assert default_score.text == "20"
        assert default_message.text == "Start guessing..."
        assert default_highscore.text == "0"

    def click_check_button(self):
        element = self.driver.find_element(*MainPageLocators.CHECK_BUTTON)
        element.click()

    def confirmation_by_enter_button(self):
        element = self.driver.find_element(*MainPageLocators.GUESS)
        element.send_keys(Keys.RETURN)

    def loop_higher_value(self, y):
        mainPage = MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = ResultPage(self.driver)

        win_number = int(mainPage.win)
        win_number += 1
        starting_score = mainPage.starting_score
        for a in range(y):
            x = random.randint(win_number, 20)
            mainPage.input_value = x
            mainPage.click_check_button()
            starting_score -= 1
            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_response_after_checked_higher_value(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

    def loop_lower_value(self, y):
        mainPage = MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = ResultPage(self.driver)

        win_number = int(mainPage.win)
        win_number -= 1
        starting_score = mainPage.starting_score
        for a in range(y):
            x = random.randint(1, win_number)
            mainPage.input_value = x
            mainPage.click_check_button()
            starting_score -= 1

            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_response_after_checked_lower_value(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

    def background_color(self):
        color = self.driver.find_element(*MainPageLocators.BACKGROUND_COLOR)
        return color.value_of_css_property("background-color")

    def number(self):
        width = self.driver.find_element(*MainPageLocators.NUMBER)
        return width

class ResultPage(BasePage):

    def message_response_after_checked_value_out_of_range(self):
        return "Really to high!"

    def message_response_after_checked_higher_value(self):
        return "To high!"

    def message_response_after_checked_lower_value(self):
        return "To low!"

    def message_response_after_win(self):
        return "You win!!"

    def message_response_after_defeat(self):
        return "You lost!"

    def message_no_value_response(self):
        return "No number!"

    def score_after_1_mistake(self):
        return "19"

    def score_after_3_mistakes(self):
        return "17"

    def score_after_5_mistakes(self):
        return "15"

    def score_after_6_mistakes(self):
        return "14"

    def score_after_defeat(self):
        return "0"

    def highscore_after_5_mistake(self):
        return "15"

    def highscore_after_3_mistake(self):
        return "17"
