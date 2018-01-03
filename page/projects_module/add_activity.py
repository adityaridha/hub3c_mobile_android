from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility


raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]

class AddActivity():
    activity_parent = "au.geekseat.com.hub3candroid:id/spinner_parent_activity"
    activity_predecessor = "au.geekseat.com.hub3candroid:id/edit_predecessors"
    activity_subject = "au.geekseat.com.hub3candroid:id/et_subject"
    activity_type = "au.geekseat.com.hub3candroid:id/spinner_activity_type"
    activity_description = "au.geekseat.com.hub3candroid:id/et_description"
    activity_budget = "au.geekseat.com.hub3candroid:id/et_activity_budget"
    activity_budget_hours = "au.geekseat.com.hub3candroid:id/et_activity_hours"
    activity_sequence = "au.geekseat.com.hub3candroid:id/spinner_sequence"
    activity_assignee = "au.geekseat.com.hub3candroid:id/spinner_assigned_to"
    activity_status = "au.geekseat.com.hub3candroid:id/spinner_status"
    activity_status_update = "au.geekseat.com.hub3candroid:id/et_status_update"
    activity_progress_bar = "au.geekseat.com.hub3candroid:id/seek_progress"
    activity_progress = "au.geekseat.com.hub3candroid:id/tv_progress"
    activity_priority = "au.geekseat.com.hub3candroid:id/spinner_priority"
    activity_proposed_start_date = "au.geekseat.com.hub3candroid:id/et_date_start"
    activity_proposed_start_time = "au.geekseat.com.hub3candroid:id/et_time_start"
    activity_proposed_finish_date = "au.geekseat.com.hub3candroid:id/et_date_finish"
    activity_proposed_finish_time = "au.geekseat.com.hub3candroid:id/et_time_finish"
    activity_actual_start_date = "au.geekseat.com.hub3candroid:id/et_date_actual_start"
    activity_actual_start_time = "au.geekseat.com.hub3candroid:id/et_time_actual_start"
    activity_actual_finish_date = "au.geekseat.com.hub3candroid:id/et_date_completed"
    activity_actual_finish_time = "au.geekseat.com.hub3candroid:id/et_time_completed"
    activity_reminder_date = "au.geekseat.com.hub3candroid:id/et_date_reminder"
    activity_reminder_time = "au.geekseat.com.hub3candroid:id/et_time_reminder"
    activity_mark_completed = "au.geekseat.com.hub3candroid:id/switch_marks_as_complete"
    activity_is_billable = "au.geekseat.com.hub3candroid:id/switch_is_billable"
    add_activity_button = "au.geekseat.com.hub3candroid:id/btn_add"
    form_title = "//*[@text='Add Activity']"
    success_message = "" #GANTI!!!


    def __init__(self, driver):
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.form_title)))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.activity_parent)))
            print("Create activity is ready")
        except TimeoutException:
            print("Create activity is not ready")

    def input_activity_subject(self):
        self.driver.find_element_by_id(self.activity_subject).send_keys("Automated Activity {}".format(date))

    def select_activity_type(self):
        activity_type = self.driver.find_element_by_id(self.activity_type)
        activity_type.click()
        self.util.tap_first_result_auto_complete(activity_type)
        time.sleep(1)

    def select_activity_sequence(self):
        activity_sequence = self.driver.find_element_by_id(self.activity_sequence)
        activity_sequence.click()
        self.util.tap_first_result_auto_complete(activity_sequence)
        time.sleep(1)

    def input_activity_assignee(self):
        activity_assignee = self.driver.find_element_by_id(self.activity_assignee)
        activity_assignee.click()
        self.util.tap_first_result_auto_complete(activity_assignee)

    def select_activity_status(self):
        activity_status = self.driver.find_element_by_id(self.activity_status)
        activity_status.click()
        self.util.tap_first_result_auto_complete(activity_status)
        time.sleep(1)

    def select_activity_priority(self):
        activity_priority = self.driver.find_element_by_id(self.activity_priority)
        activity_priority.click()
        self.util.tap_first_result_auto_complete(activity_priority)
        time.sleep(1)

    def input_activity_desc(self):
        self.driver.find_element_by_id(self.activity_description).send_keys("This activity is from automation")

    def set_proposed_start_date(self):
        self.driver.find_element_by_id(self.activity_proposed_start_date).click()
        time.sleep(1)

        # PILIH HARI?

        self.driver.find_element_by_xpath("//*[@text='2018']").click()  # harus diganti locator nya

        # //*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_proposed_start_time(self):
        self.driver.find_element_by_id(self.activity_proposed_start_time).click()
        time.sleep(1)

        # PILIH JAM?

        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()


    def set_actual_start_date(self):
        self.driver.find_element_by_id(self.activity_actual_start_date).click()
        time.sleep(1)

        # PILIH HARI?

        self.driver.find_element_by_xpath("//*[@text='2018']").click()
        # //*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_actual_start_time(self):
        self.driver.find_element_by_id(self.activity_actual_start_time).click()
        time.sleep(1)

        # PILIH JAM?

        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_is_billable(self):
        self.driver.find_element_by_id(self.activity_is_billable).click()

    def set_is_complete(self):
        self.driver.find_element_by_id(self.activity_mark_completed).click()

    def tap_add_activity(self):
        self.driver.find_element_by_id(self.add_activity_button).click()

    def verify_activity(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, self.success_message)))
            print("Add Activity is successful")
        except TimeoutException:
            print("Add Activity is unsuccessful")
            pytest.fail()