import unittest
from utilities.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginPage(unittest.TestCase):

    log = Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.go_btn = 'submit'
        self.email_input = 'email'
        self.signup_btn = "//*[contains(text(),'Signup / Login')]"
        self.password_input = 'password'
        self.login_btn = "//button[contains(text(),'Login')]"
        self.incorrect_creds = "//p[contains(text(), 'Your email or password is incorrect!')]"

    def validate_url(self,url):
        self.assertTrue("URL is incorrect", url)
        self.log.info('Url validated')

    def click_on_signup(self):
        """
        Click on the 'Sign up / Login' button
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.signup_btn)))
        element.click()
        self.log.info('Clicked on Sign up / Login')

    def click_on_search(self):
        """
        Click on the 'Go' button
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.go_btn)))
        element.click()
        self.log.info('Clicked on Go')

    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, self.email_input)))
        element.send_keys(email)
        self.log.info('Entered email')

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, self.password_input)))
        element.send_keys(password)
        self.log.info('Entered password')

    def click_on_login(self):
        """
        Clicks on the 'Login' button
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))
        element.click()
        self.log.info('Clicked on login')
    
    def validate_login_error(self):
        """
        Validates that and error is displayed when entering incorrect credentials
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.incorrect_creds)))
        self.assertTrue(element.is_displayed())
        self.log.info('Error validated')
