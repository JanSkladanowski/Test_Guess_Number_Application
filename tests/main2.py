import unittest
from selenium import webdriver
import page
import random
from selenium.webdriver.support.color import Color


class TestScenario1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\Nowy folder\moje\programowanie\seleniumDr\97.0.4692.71\chromedriver.exe")
        self.driver.get(r"http://127.0.0.1:5500/index.html")

    def test_win(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        win_number = int(mainPage.win)
        number_width_before = mainPage.number().value_of_css_property("width")

        mainPage.input_value = win_number
        mainPage.click_check_button()

        page_background_color = mainPage.background_color()
        number_width_after = mainPage.number().value_of_css_property("width")
        number_value = int(mainPage.number().text)
        page_message = mainPage.message
        page_score = mainPage.score
        page_highscore = mainPage.highscore
        page_should_response = page.ResultPage(self.driver)

        self.assertEqual(page_message, page_should_response.message_response_after_win())
        self.assertEqual(page_score, "20")
        self.assertEqual(page_highscore, "20")
        self.assertNotEqual(number_width_before, number_width_after)
        self.assertEqual(number_value, win_number)
        self.assertEqual(Color.from_string(f"{page_background_color}").hex, "#60b347")

    def test_win2(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        win_number = int(mainPage.win)
        number_width_before = mainPage.number().value_of_css_property("width")
        starting_score = mainPage.starting_score

        for a in range(3):
            x = random.randint(1, 20)
            if x == win_number:
                x -= 1
            else:
                pass

            mainPage.input_value = x
            mainPage.click_check_button()
            starting_score -= 1

            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            if x > win_number:
                self.assertEqual(page_should_response.message_response_after_checked_higher_value(), page_message)
            else:
                self.assertEqual(page_should_response.message_response_after_checked_lower_value(), page_message)

            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

        mainPage.input_value = win_number
        mainPage.click_check_button()

        page_background_color = mainPage.background_color()
        number_width_after = mainPage.number().value_of_css_property("width")
        number_value = int(mainPage.number().text)
        page_message = mainPage.message
        page_score = mainPage.score
        page_highscore = mainPage.highscore
        page_should_response = page.ResultPage(self.driver)

        self.assertEqual(page_message, page_should_response.message_response_after_win())
        self.assertEqual(page_score, page_should_response.score_after_3_mistakes())
        self.assertEqual(page_highscore, page_should_response.highscore_after_3_mistake())
        self.assertNotEqual(number_width_before, number_width_after)
        self.assertEqual(number_value, win_number)
        self.assertEqual(Color.from_string(f"{page_background_color}").hex, "#60b347")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
