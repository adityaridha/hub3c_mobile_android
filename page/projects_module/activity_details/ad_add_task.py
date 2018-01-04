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

class AddTask():
    task_subject = "au.geekseat.com.hub3candroid:id/et_subject"
    task_predecessor = "au.geekseat.com.hub3candroid:id/edit_predecessors"
    task_type = "au.geekseat.com.hub3candroid:id/spinner_activity_type"
    task_description = "au.geekseat.com.hub3candroid:id/et_description"
    task_budget = "au.geekseat.com.hub3candroid:id/et_activity_budget"
    task_budget_hours = "au.geekseat.com.hub3candroid:id/et_activity_hours"
    task_sequence = "au.geekseat.com.hub3candroid:id/spinner_sequence"
    task_assignee = "au.geekseat.com.hub3candroid:id/spinner_assigned_to"
    task_status = "au.geekseat.com.hub3candroid:id/spinner_status"
    task_status_update = "au.geekseat.com.hub3candroid:id/et_status_update"
    task_progress_bar = "au.geekseat.com.hub3candroid:id/seek_progress"
    task_progress = "au.geekseat.com.hub3candroid:id/tv_progress"
    task_priority = "au.geekseat.com.hub3candroid:id/spinner_priority"
    task_proposed_start_date = "au.geekseat.com.hub3candroid:id/et_date_start"
    task_proposed_start_time = "au.geekseat.com.hub3candroid:id/et_time_start"
    task_proposed_finish_date = "au.geekseat.com.hub3candroid:id/et_date_finish"
    task_proposed_finish_time = "au.geekseat.com.hub3candroid:id/et_time_finish"
    task_actual_start_date = "au.geekseat.com.hub3candroid:id/et_date_actual_start"
    task_actual_start_time = "au.geekseat.com.hub3candroid:id/et_time_actual_start"
    task_actual_finish_date = "au.geekseat.com.hub3candroid:id/et_date_completed"
    task_actual_finish_time = "au.geekseat.com.hub3candroid:id/et_time_completed"
    task_reminder_date = "au.geekseat.com.hub3candroid:id/et_date_reminder"
    task_reminder_time = "au.geekseat.com.hub3candroid:id/et_time_reminder"
    task_mark_completed = "au.geekseat.com.hub3candroid:id/switch_marks_as_complete"
    task_is_billable = "au.geekseat.com.hub3candroid:id/switch_is_billable"
    add_task_button = "au.geekseat.com.hub3candroid:id/btn_add"
    form_title = "//*[@text='Add Task']"
    success_add_task = "" #GANTI!!!

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.form_title)))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.task_subject)))
            print("Create task is ready")
        except TimeoutException:
            print("Create task is not ready")

    def input_task_subject(self):
        self.driver.find_element_by_id(self.task_subject).send_keys("Automated Task {}".format(date))

    def select_task_type(self):
        task_type = self.driver.find_element_by_id(self.task_type)
        task_type.click()
        self.util.tap_first_result_auto_complete(task_type)
        time.sleep(1)

    def select_task_sequence(self):
        task_sequence = self.driver.find_element_by_id(self.task_sequence)
        task_sequence.click()
        self.util.tap_first_result_auto_complete(task_sequence)
        time.sleep(1)

    def select_task_status(self):
        task_status = self.driver.find_element_by_id(self.task_status)
        task_status.click()
        self.util.tap_first_result_auto_complete(task_status)
        time.sleep(1)

    def select_task_priority(self):
        task_priority = self.driver.find_element_by_id(self.task_priority)
        task_priority.click()
        self.util.tap_first_result_auto_complete(task_priority)
        time.sleep(1)

    def input_task_desc(self):
        self.driver.find_element_by_id(self.task_description).send_keys("This task is from automation")

    def set_proposed_start_date(self):
        self.driver.find_element_by_id(self.task_proposed_start_date).click()
        time.sleep(1)

        # PILIH HARI?

        self.driver.find_element_by_xpath("//*[@text='2018']").click()  # harus diganti locator nya

        # //*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_proposed_start_time(self):
        self.driver.find_element_by_id(self.task_proposed_start_time).click()
        time.sleep(1)

        # PILIH JAM?

        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def input_task_assignee(self):
        task_assignee = self.driver.find_element_by_id(self.task_assignee)
        task_assignee.click()
        self.util.tap_first_result_auto_complete(task_assignee)

    def set_actual_start_date(self):
        self.driver.find_element_by_id(self.task_actual_start_date).click()
        time.sleep(1)

        # PILIH HARI?

        self.driver.find_element_by_xpath("//*[@text='2018']").click()
        # //*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_actual_start_time(self):
        self.driver.find_element_by_id(self.task_actual_start_time).click()
        time.sleep(1)

        # PILIH JAM?

        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_is_billable(self):
        self.driver.find_element_by_id(self.task_is_billable).click()

    def set_is_complete(self):
        self.driver.find_element_by_id(self.task_mark_completed).click()

    def tap_add_task(self):
        self.driver.find_element_by_id(self.add_task_button).click()

    def verify_task(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, self.success_add_task)))
            print("Add Task is successful")
        except TimeoutException:
            print("Add Task is unsuccessful")
            pytest.fail()