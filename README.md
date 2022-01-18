# Test_Guess_Number_Application

This is a project for showcasing my ability to test a web application. This web application was created with html, css and JavaScript. Tests are created in Python 3.10.0 and framework selenium 4.0.0 (Before You run test You have to install selenium)

I created this project because I wanted to introduce myself to technology such as Git. I also wanted to show my skills in Python, JS, HTML and CSS.

APPLICATION This application is a simple game application, where user has to guess random generated number. Application have 1 guess space for input our value. Application have 2 buttons:

"Again" to restart aplication.

"Check!" to compare our value with random generatedly application value.

For testing purposes, application stores a randomly generated value in upper left corner.

After confirming the wrong number in the guessing field with "Check!" button, the application should return the message: "To low!" or "To high", and the score value should go down by 1

If You confirmed winning value in guess box by "Check!" button, application should return message : "You win!", the highscore value should be replaced with score value, the background should change colour, the number box should be wider, and instead of "?" number box should contain winning value

If You win but Your score value is less than highscore value, a highscore value should not be changed

If You won, and after that You clicked on "Again!" button, everything should return to default settings except highscore value.

I recomend to open html file on port 5500

TESTS

In testy.pdf there are a scenarios and test cases in polish language.
In Raport_bledow.pdf there are reports about bugs in polish language.
In tests.pdf there are a scenarios and test cases in english language. (This file will be soon)
In Bugs_report.pdf there are reports about bugs in english language. (This file will be soon)
Folder tests contain all python files which You need to do automated tests.
Tests are made in Chrome browser, so if You don't have Chrome browser You have to download it.
You have to download drivers.exe for your browser version, and put a path to your drivers.exe in each main#.py in place of PATH TO DRIVER.
If You open application on different port, You have to change self.driver.get("http://127.0.0.1:5500/index.html") in each main#.py
