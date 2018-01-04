from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page
import datetime
import pytz
import time

class AddActivity(Page):
    activity_parent = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_parent_activity")
    activity_predecessor = (By.ID, "au.geekseat.com.hub3candroid:id/edit_predecessors")
    activity_subject = (By.ID, "au.geekseat.com.hub3candroid:id/et_subject")
    activity_type = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_activity_type")
    activity_description = (By.ID, "au.geekseat.com.hub3candroid:id/et_description")
    activity_budget = (By.ID, "au.geekseat.com.hub3candroid:id/et_activity_budget")
    activity_budget_hours = (By.ID, "au.geekseat.com.hub3candroid:id/et_activity_hours")
    activity_sequence = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_sequence")
    activity_assignee = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_assigned_to")
    activity_status = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_status")
    activity_status_update = (By.ID, "au.geekseat.com.hub3candroid:id/et_status_update")
    activity_progress_bar = (By.ID, "au.geekseat.com.hub3candroid:id/seek_progress")
    activity_progress = (By.ID, "au.geekseat.com.hub3candroid:id/tv_progress")
    activity_priority = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_priority")
    activity_proposed_start_date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_start")
    activity_proposed_start_time = (By.ID, "au.geekseat.com.hub3candroid:id/et_time_start")
    activity_proposed_finish_date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_finish")
    activity_proposed_finish_time = (By.ID, "au.geekseat.com.hub3candroid:id/et_time_finish")
    activity_actual_start_date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_actual_start")
    activity_actual_start_time = (By.ID, "au.geekseat.com.hub3candroid:id/et_time_actual_start")
    activity_actual_finish_date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_completed")
    activity_actual_finish_time = (By.ID, "au.geekseat.com.hub3candroid:id/et_time_completed")
    activity_reminder_date = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_reminder")
    activity_reminder_time = (By.ID, "au.geekseat.com.hub3candroid:id/et_time_reminder")
    activity_mark_completed = (By.ID, "au.geekseat.com.hub3candroid:id/switch_marks_as_complete")
    activity_as_billable = (By.ID, "au.geekseat.com.hub3candroid:id/switch_is_billable")
    add_activity_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_add")


    def __init__(self):
        super().__init__()

    def input_activity_subject(self, subject):
        self.find_element(self.activity_subject).send_keys(subject)

    def select_type(self):
        type = self.find_element(self.activity_type)
        self.tap_spinner_options(spinner=type, index=2)

    def tap_proposed_start_date(self):
        self.find_element(self.activity_proposed_start_date).click()

    def input_description(self):
        self.find_element(self.activity_description).send_keys("description")

    def input_budget(self):
        self.find_element(self.activity_budget).send_keys("900")

    def input_budget_hours(self):
        self.find_element(self.activity_budget_hours).send_keys("999")




