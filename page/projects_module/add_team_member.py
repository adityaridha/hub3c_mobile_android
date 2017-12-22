from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility



class AddTeamMember():
    form_title = "//*[@text='Add Team Member']"
    team_member = "au.geekseat.com.hub3candroid:id/edit_team_member"
    team_member_options = "au.geekseat.com.hub3candroid:id/rl_title_attachments"  #??? belum bener probably
    team_role = "au.geekseat.com.hub3candroid:id/edit_project_role"
    hourly_rate_charge = "au.geekseat.com.hub3candroid:id/edit_hourly_charge"
    hourly_rate_cost = "au.geekseat.com.hub3candroid:id/edit_hourly_cost"
    is_project_owner = "au.geekseat.com.hub3candroid:id/check_owner"
    save_button = "au.geekseat.com.hub3candroid:id/button_save"
    success_add_member = "//*[@text='Team member added!']"

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.Helper(driver=self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.form_title)))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.team_member)))
            print("Add Team Member is Ready")
        except TimeoutException:
            print("Add Team Member not ready")

    def input_team_member_name(self):
        team_member_name_el = self.driver.find_element_by_id(self.team_member)
        team_member_name_el.send_keys("Anne Kirrin")
        self.util.tap_first_result_auto_complete(team_member_name_el)

    def input_team_role(self):
        self.driver.find_element_by_id(self.team_role).send_keys("Automation Role")

    def input_hourly_charge(self):
        self.driver.find_element_by_id(self.hourly_rate_charge).send_keys("1234")

    def input_hourly_cost(self):
        self.driver.find_element_by_id(self.hourly_rate_cost).send_keys("1234")

    def check_project_owner(self):
        self.driver.find_element_by_id(self.is_project_owner).click()

    def save_team_member(self):
        self.driver.find_element_by_id(self.save_button).click()

    def verify_team_member(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, self.success_add_member)))
            print("Add Team Member is successful")
        except TimeoutException:
            print("Add Team Member is unsuccessful")
            pytest.fail()
