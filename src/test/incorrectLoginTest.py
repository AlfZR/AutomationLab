import unittest
from selenium import webdriver
from time import sleep
from pageObj.AutoLoginPage import loginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

        self.loginPage = loginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_incorrect_login(self):
        self.driver.get('https://automationexercise.com')
        self.loginPage.validate_url(self.driver.current_url)
        self.loginPage.click_on_signup()
        self.loginPage.enter_email('hola@go.com')
        self.loginPage.enter_password('pass@123')
        self.loginPage.click_on_login()
        self.loginPage.validate_login_error()
        

if __name__ == '__main__':
    unittest.main()
