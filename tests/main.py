import unittest
from selenium import webdriver
import page
import random


class TestScenario1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"PATH TO DRIVER")
        self.driver.get(r"http://127.0.0.1:5500/index.html")

    def test_number_out_of_range(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        x = random.randint(21, 60)
        mainPage.input_value = x
        mainPage.click_check_button()

        page_message = mainPage.message
        page_should_response = page.ResultPage(self.driver)
        page_score = mainPage.score
        page_highscore = mainPage.highscore

        self.assertEqual(page_message, page_should_response.message_response_after_checked_value_out_of_range())
        self.assertEqual(page_score, page_should_response.score_after_1_mistake())
        self.assertEqual(page_highscore, "0")

    def test_score_1x_random_higher_value_accepted_by_ENTER(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        win_number = int(mainPage.win)
        win_number += 1
        x = random.randint(win_number, 20)
        mainPage.input_value = x
        mainPage.confirmation_by_enter_button()

        page_message = mainPage.message
        page_should_response = page.ResultPage(self.driver)
        page_score = mainPage.score
        page_highscore = mainPage.highscore

        self.assertEqual(page_message, page_should_response.message_response_after_checked_higher_value(), "Enter button doesn't work")
        self.assertEqual(page_score, page_should_response.score_after_1_mistake())
        self.assertEqual(page_highscore, "0")

    def test_score_1x_random_text_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        x = random.choice("xx")
        mainPage.input_value = x
        mainPage.click_check_button()

        page_message = mainPage.message
        page_should_response = page.ResultPage(self.driver)
        page_score = mainPage.score
        page_highscore = mainPage.highscore

        self.assertEqual(page_message, page_should_response.message_no_value_response())
        self.assertEqual(page_score, page_should_response.score_after_1_mistake())
        self.assertEqual(page_highscore, "0")

    def test_score_1x_random_higher_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        win_number = int(mainPage.win)
        win_number += 1
        x = random.randint(win_number, 20)
        mainPage.input_value = x
        mainPage.click_check_button()

        page_message = mainPage.message
        page_should_response = page.ResultPage(self.driver)
        page_score = mainPage.score
        page_highscore = mainPage.highscore

        self.assertEqual(page_message, page_should_response.message_response_after_checked_higher_value())
        self.assertEqual(page_score, page_should_response.score_after_1_mistake())
        self.assertEqual(page_highscore, "0")

    def test_score_5x_random_higher_value(self):
        page.MainPage.loop_higher_value(self, 5)

        mainPage = page.MainPage(self.driver)
        page_should_response = page.ResultPage(self.driver)

        final_page_score = mainPage.score
        final_page_message = mainPage.message
        final_page_highscore = mainPage.highscore

        self.assertEqual(final_page_message, page_should_response.message_response_after_checked_higher_value())
        self.assertEqual(final_page_score, page_should_response.score_after_5_mistakes())
        self.assertEqual(final_page_highscore, "0")

    def test_score_3x_random_higher_value(self):
        page.MainPage.loop_higher_value(self, 3)

        mainPage = page.MainPage(self.driver)
        page_should_response = page.ResultPage(self.driver)

        final_page_score = mainPage.score
        final_page_message = mainPage.message
        final_page_highscore = mainPage.highscore

        self.assertEqual(final_page_message, page_should_response.message_response_after_checked_higher_value())
        self.assertEqual(final_page_score, page_should_response.score_after_3_mistakes())
        self.assertEqual(final_page_highscore, "0")

    def test_score_1x_random_lower_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()

        win_number = int(mainPage.win)
        win_number -= 1
        x = random.randint(1, win_number)
        mainPage.input_value = x
        mainPage.click_check_button()

        page_message = mainPage.message
        page_should_response = page.ResultPage(self.driver)
        page_score = mainPage.score
        page_highscore = mainPage.highscore

        self.assertEqual(page_message, page_should_response.message_response_after_checked_lower_value())
        self.assertEqual(page_score, page_should_response.score_after_1_mistake())
        self.assertEqual(page_highscore, "0")

    def test_score_3x_random_lower_value(self):
        page.MainPage.loop_lower_value(self, 3)

        mainPage = page.MainPage(self.driver)
        page_should_response = page.ResultPage(self.driver)

        final_page_score = mainPage.score
        final_page_message = mainPage.message
        final_page_highscore = mainPage.highscore

        self.assertEqual(final_page_message, page_should_response.message_response_after_checked_lower_value())
        self.assertEqual(final_page_score, page_should_response.score_after_3_mistakes())
        self.assertEqual(final_page_highscore, "0")

    def test_score_3x_random_lower_higher_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        win_number = int(mainPage.win)
        lower_win_number = win_number - 1
        higher_win_number = win_number + 1
        starting_score = mainPage.starting_score
        for a in range(3):
            x = random.randint(1, lower_win_number)
            xx = random.randint(higher_win_number, 20)
            mainPage.input_value = x
            mainPage.click_check_button()
            starting_score -= 1

            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_response_after_checked_lower_value(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

            mainPage.input_value = xx
            mainPage.click_check_button()
            starting_score -= 1
            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_response_after_checked_higher_value(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

        final_page_score = mainPage.score
        final_page_message = mainPage.message
        final_page_highscore = mainPage.highscore

        self.assertEqual(final_page_message, page_should_response.message_response_after_checked_higher_value())
        self.assertEqual(final_page_score, page_should_response.score_after_6_mistakes())
        self.assertEqual(final_page_highscore, "0")

    def test_3_times_empty_value(self):
        mainPage = page.MainPage(self.driver)
        mainPage.default_conditions()
        page_should_response = page.ResultPage(self.driver)

        starting_score = mainPage.starting_score
        for a in range(3):
            mainPage.click_check_button()
            starting_score -= 1
            page_score = mainPage.score
            page_message = mainPage.message
            page_highscore = mainPage.highscore

            self.assertEqual(page_should_response.message_no_value_response(), page_message)
            self.assertEqual(starting_score, int(page_score))
            self.assertEqual(page_highscore, "0")

        final_page_score = mainPage.score
        final_page_message = mainPage.message
        final_page_highscore = mainPage.highscore

        self.assertEqual(final_page_message, page_should_response.message_no_value_response())
        self.assertEqual(final_page_score, page_should_response.score_after_3_mistakes())
        self.assertEqual(final_page_highscore, "0")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
