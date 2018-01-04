from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
import time
from page.base_page import Page

class ArchivedProjects():
    project_title = (By.ID, "au.geekseat.com.hub3candroid:id/title")
    project_last_state = (By.ID, "au.geekseat.com.hub3candroid:id/textInprogress")
    project_archived_date = (By.ID, "au.geekseat.com.hub3candroid:id/textDate")
    restore_button = (By.ID, "au.geekseat.com.hub3candroid:id/textDueDate")
    restore_message = (By.XPATH, "//*[@text='Are you sure you want to restore this project?']")
    restore_ok = (By.ID, "android:id/button1")
    restore_cancel = (By.ID, "android:id/button2")
    success_restore_text = (By.XPATH, "//*[@text='Project is successfully restored']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def tap_restore_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.restore_button))
        except TimeoutException:
            print("Restore project not ready")
        self.driver.find_element(self.restore_button).click()

    def proceed_restore_project(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(self.restore_message))
            self.driver.find_element(self.restore_ok).click()
        except TimeoutException:
            print("Restore project confirmation does not appear")
            pytest.fail()

    def verify_restore_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.success_restore_text))
            print("Restore project success")
        except TimeoutException:
            print("Restore project failed")
            pytest.fail()