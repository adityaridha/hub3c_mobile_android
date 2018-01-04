from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import pytest


class Login(Page):

    username_field = (By.ID, 'au.geekseat.com.hub3candroid:id/textUsername')
    password_field = (By.ID, 'au.geekseat.com.hub3candroid:id/textPassword')
    sign_in_button = (By.ID, 'au.geekseat.com.hub3candroid:id/buttonLogin')
    reg_forgot_password = (By.ID, "au.geekseat.com.hub3candroid:id/textForgotPassword")
    hub3c_logo = (By.CLASS_NAME, "android.widget.ImageView")
    login_failed_text = (By.XPATH, "//*[@text='Wrong Email or Password']")

    def __init__(self):
        super().__init__()

    def verified_all_element(self, reset=True):
        if reset == True:
            self.driver.launch_app()
        try:
            self.find_element(self.username_field)
            self.find_element(self.password_field)
            self.find_element(self.sign_in_button)
            print("Login page successfully loaded")
        except TimeoutException:
            pytest.fail("Login Page Not Successfully loaded")

    def login(self, email, password):
        self.find_element(self.username_field).send_keys(email)
        self.find_element(self.password_field).send_keys(password)
        self.find_element(self.sign_in_button).click()

    def input_email(self, email):
        self.find_element(self.username_field).send_keys(email)

    def input_password(self, password):
        self.find_element(self.password_field).send_keys(password)

    def tap_sign_in(self):
        self.find_element(self.sign_in_button).click()

    def tap_registration(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.reg_forgot_password)))
        except TimeoutException:
            print("element not ready")

        register =  self.driver.find_element_by_id(self.reg_forgot_password)
        x = register.location['x']
        y = register.location['y']
        positions = []
        positions.append((x + 10, y))
        positions.append((x + 20, y))
        self.driver.tap(positions)

    def tap_forgot_password(self):

        forgot_pass =  self.driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textForgotPassword')
        x = forgot_pass.location['x']
        y = forgot_pass.location['y']
        # height = forgot_pass.size['height']
        width = forgot_pass.size['width']

        positions = []
        positions.append((x + width - 20, y))
        positions.append((x + width - 10, y))
        print("click forgot password")
        self.driver.tap(positions)

    def verify_login_is_failed(self):
        self.find_element(self.login_failed_text)