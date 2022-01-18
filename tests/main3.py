import unittest
from selenium import webdriver
import page
import random


class TestScenario3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"PATH TO DRIVER")
        self.driver.get(r"http://127.0.0.1:5500/index.html")

    def test_lost(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        win_number = int(mainPage.win)
        starting_score = mainPage.starting_score

        for a in range(19):
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

        x = random.randint(1, 20)
        if x == win_number:
            x -= 1
        else:
            pass

        mainPage.input_value = x
        mainPage.click_check_button()
        starting_score -= 1

        page_message = mainPage.message
        page_score = mainPage.score
        page_highscore = mainPage.highscore
        page_should_response = page.ResultPage(self.driver)

        self.assertEqual(page_message, page_should_response.message_response_after_defeat())
        self.assertEqual(page_score, page_should_response.score_after_defeat())
        self.assertEqual(page_highscore, "0")

    def test_lose_empty_value_x20(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        win_number = int(mainPage.win)
        starting_score = mainPage.starting_score

        for a in range(19):
            mainPage.click_check_button()
            starting_score -= 1

            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_no_value_response(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

        mainPage.click_check_button()
        starting_score -= 1

        page_message = mainPage.message
        page_score = mainPage.score
        page_highscore = mainPage.highscore
        page_should_response = page.ResultPage(self.driver)

        self.assertEqual(page_message, page_should_response.message_response_after_defeat())
        self.assertEqual(page_score, page_should_response.score_after_defeat())
        self.assertEqual(page_highscore, "0")

    def test_27x_random_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        win_number = int(mainPage.win)
        starting_score = mainPage.starting_score

        for a in range(19):
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

        for a in range(8):
            x = random.randint(1, 20)
            if x == win_number:
                x -= 1
            else:
                pass

            mainPage.input_value = x
            mainPage.click_check_button()
            starting_score -= 1

            page_message = mainPage.message
            page_score = mainPage.score
            page_highscore = mainPage.highscore
            page_should_response = page.ResultPage(self.driver)

            self.assertEqual(page_message, page_should_response.message_response_after_defeat())
            self.assertEqual(page_score, page_should_response.score_after_defeat())
            self.assertEqual(page_highscore, "0")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
