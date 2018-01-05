from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility
from page.base_page import Page



class EditActivityTimesheet():
    form_title = (By.XPATH, "")
    team_member = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_team_member")
    activity = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_activity")
    date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_entered")
    hours_spent = (By.ID, "au.geekseat.com.hub3candroid:id/et_hours_spent")
    remaining_days = (By.ID, "au.geekseat.com.hub3candroid:id/et_days_remaining")
    update_timesheet_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_add")
    success_edit_timesheet = (By.XPATH, "")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.util = utility.StepHelper(driver=self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.form_title))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(self.team_member))
            print("Edit Timesheet is Ready")
        except TimeoutException:
            print("Edit Timesheet not ready")

    def input_date(self):
        self.driver.find_element(self.date).click()
        time.sleep(1)
        # PILIH HARI?
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def save_timesheet(self):
        self.driver.find_element(self.update_timesheet_button).click()

    def verify_timesheet(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located(self.success_edit_timesheet))
            print("Edit Timesheet is successful")
        except TimeoutException:
            print("Edit Timesheet is unsuccessful")
            pytest.fail()