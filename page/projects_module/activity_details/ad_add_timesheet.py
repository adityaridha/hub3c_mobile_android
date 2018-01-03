from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility


class AddActivityTimesheet():
    form_title = ""
    team_member = "au.geekseat.com.hub3candroid:id/spinner_team_member"
    activity = "au.geekseat.com.hub3candroid:id/spinner_activity"
    date = "au.geekseat.com.hub3candroid:id/et_date_entered"
    hours_spent = "au.geekseat.com.hub3candroid:id/et_hours_spent"
    remaining_days = "au.geekseat.com.hub3candroid:id/et_days_remaining"
    add_timesheet_button = "au.geekseat.com.hub3candroid:id/btn_add"
    success_message = ""

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.Helper(driver=self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.form_title)))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.team_member)))
            print("Add Timesheet is Ready")
        except TimeoutException:
            print("Add Timesheet not ready")

    def input_team_member_name(self):
        team_member_name_el = self.driver.find_element_by_id(self.team_member)
        team_member_name_el.send_keys("Anne Kirrin")
        self.util.tap_first_result_auto_complete(team_member_name_el)

    def input_activity(self):
        activity = self.driver.find_element_by_id(self.activity)
        activity.click()
        time.sleep(1)
        self.util.tap_first_result_auto_complete(activity)

    def input_date(self):
        self.driver.find_element_by_id(self.date).click()
        time.sleep(1)
        # PILIH HARI?
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def save_timesheet(self):
        self.driver.find_element_by_id(self.add_timesheet_button).click()

    def verify_timesheet(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, self.success_message)))
            print("Add Timesheet is successful")
        except TimeoutException:
            print("Add Timesheet is unsuccessful")
            pytest.fail()