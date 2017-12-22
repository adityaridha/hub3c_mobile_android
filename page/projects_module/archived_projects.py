from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
import time


class ArchivedProjects():
    project_title = "au.geekseat.com.hub3candroid:id/title"
    project_last_state = "au.geekseat.com.hub3candroid:id/textInprogress"
    project_archived_date = "au.geekseat.com.hub3candroid:id/textDate"
    restore_button = "au.geekseat.com.hub3candroid:id/textDueDate"
    restore_message = "//*[@text='Are you sure you want to restore this project?']"
    restore_ok = "android:id/button1"
    restore_cancel = "android:id/button2"
    success_restore_text = "//*[@text='Project is successfully restored']"

    def __init__(self, driver):
        self.driver = driver

    def tap_restore_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.restore_button)))
        except TimeoutException:
            print("Restore project not ready")
        self.driver.find_element_by_id(self.restore_button).click()

    def proceed_restore_project(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,self.restore_message)))
            self.driver.find_element_by_id(self.restore_ok).click()
        except TimeoutException:
            print("Restore project confirmation does not appear")
            pytest.fail()

    def verify_restore_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.success_restore_text)))
            print("Restore project success")
        except TimeoutException:
            print("Restore project failed")
            pytest.fail()