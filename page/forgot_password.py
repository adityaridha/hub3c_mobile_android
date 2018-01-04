from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
from page import Page
import pytest


class ForgotPassword(Page):


    email = (By.ID, "au.geekseat.com.hub3candroid:id/editEmail")
    reset_btn = (By.ID, "au.geekseat.com.hub3candroid:id/buttonReset")
    warning_unregistered_email = (By.XPATH, "//*[@text='The Email you entered does not exist. Please try again.']")
    success_message = (By.XPATH, "//*[@text='Email has been sent to the address']")
    ignore_software_update = (By.ID, "android:id/button2")
    update_available_text = (By.XPATH, "//*[@text='Update Available']")



    def __init__(self):
        super().__init__()

    def verify_page(self):
        self.handle_software_update()
        self.find_element(self.email)
        self.find_element(self.reset_btn)


    def input_email(self, email):
        self.find_element(self.email).send_keys(email)

    def click_reset_button(self):
        self.find_element(self.reset_btn).click()

    def verify_success_message(self):
        self.find_element(self.success_message)
        print("forgot password success")

    def verify_failed_message(self):
        self.find_element(self.warning_unregistered_email)
        print("Email not found and not sent as intended")

    def handle_software_update(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(self.update_available_text))
            self.find_element(self.ignore_software_update).click()
        except:
            print("No software update")
