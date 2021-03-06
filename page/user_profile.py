from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import pytest


class UserProfile(Page):


    logout = (By.ID, "au.geekseat.com.hub3candroid:id/buttonLogout")
    switch_account = "au.geekseat.com.hub3candroid:id/buttonSwitch"
    edit = "au.geekseat.com.hub3candroid:id/action_edit"
    back = "//*[@contentDescription='Navigate up']"

    def __init__(self):
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.logout))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.switch_account)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.edit)))
            print("Dadshboard page is compleately loaded")
        except TimeoutException:
            print("element not ready")

    def tap_logout(self):
        self.find_element(self.logout).click()