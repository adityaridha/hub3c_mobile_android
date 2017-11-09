from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]

class CreateNewProject():


    form_title = "//*[@text='New Project: Overview']"
    project_name = "au.geekseat.com.hub3candroid:id/edit_project_name"
    project_code = "au.geekseat.com.hub3candroid:id/edit_project_code"
    project_desc = "au.geekseat.com.hub3candroid:id/edit_description"
    currency = "au.geekseat.com.hub3candroid:id/spinner_currency"
    status = "au.geekseat.com.hub3candroid:id/spinner_status"
    proposed_start = "au.geekseat.com.hub3candroid:id/edit_proposed_start"
    proposed_end = "au.geekseat.com.hub3candroid:id/edit_proposed_end"
    actual_start = "au.geekseat.com.hub3candroid:id/edit_actual_start"
    date_completed = "au.geekseat.com.hub3candroid:id/edit_date_complete"

    date_picker_day = "au.geekseat.com.hub3candroid:id/date_picker_day"
    day_today = "//*[@contentDescription='06 October 2017 selected']"

    reminder_date = "au.geekseat.com.hub3candroid:id/edit_reminder_date"
    billing_type = "au.geekseat.com.hub3candroid:id/spinner_billing_type"

    next = "au.geekseat.com.hub3candroid:id/ms_stepNextButton"

    ''' team member section '''

    team_member_sec_title = "//*[@text='New Project: Add Member']"
    team_member_name = "au.geekseat.com.hub3candroid:id/add_team_member"
    project_role = "au.geekseat.com.hub3candroid:id/edit_project_role"
    hourly_rate_charge = "au.geekseat.com.hub3candroid:id/edit_hourly_charge"
    hourly_rate_cost = "au.geekseat.com.hub3candroid:id/edit_hourly_cost"
    is_project_owner = "au.geekseat.com.hub3candroid:id/check_owner"
    add_team_member_button = "au.geekseat.com.hub3candroid:id/button_save"

    team_member_hourly_validation = "android:id/message"
    yes_button = "android:id/button1"
    no_button = "android:id/button2"

    ''' activity section '''

    add_activity_title = "//*[@text='New Project: Add Activities']"
    activity_description = "au.geekseat.com.hub3candroid:id/et_description"
    activity_type = "au.geekseat.com.hub3candroid:id/spinner_activity_type"
    schedule_start = "au.geekseat.com.hub3candroid:id/et_date_start"
    complete_button = "au.geekseat.com.hub3candroid:id/ms_stepCompleteButton"
    save_activity = "au.geekseat.com.hub3candroid:id/btn_add"
    cancel = "au.geekseat.com.hub3candroid:id/btn_cancel"
    activity_validation = "android:id/message"

    def __init__(self, driver):
        self.driver = driver

    def verified_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.form_title)))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.ID, self.project_name)))
        except TimeoutException:
            print("element not ready")

    def input_project_title(self):
        self.driver.find_element_by_id(self.project_name).send_keys("Appium Project {}".format(date))

    def input_project_code(self):
        self.driver.find_element_by_id(self.project_code).send_keys("Ap12")

    def input_project_desc(self):
        self.driver.find_element_by_id(self.project_desc).send_keys("This project is from automation")

    def set_reminder_date(self):
        self.driver.find_element_by_id(self.reminder_date).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click()

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def swipe_to_buttom(self):

        # y2 = 200 for 768x1280 screen, for smaller screen use higher value
        try:
            self.driver.swipe(522, 800, 495, 200, 1000)
        except :
            print("swipe sukses")

    def tap_next(self):
        print("next")
        self.driver.find_element_by_id(self.next).click()

    def tap_complete(self):
        print("tap complete")
        self.driver.find_element_by_id(self.complete_button).click()


    def handle_team_member_validation(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.team_member_hourly_validation)))
            self.driver.find_element_by_id(self.yes_button).click()
        except TimeoutException:
            print("No hourly rate warning")


    def handle_activity_validation(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.team_member_hourly_validation)))
            self.driver.find_element_by_id(self.yes_button).click()
        except TimeoutException:
            print("No hourly rate warning")


    def input_team_member_name(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.team_member_sec_title)))
            print("Add team member page is ready")
        except TimeoutException:
            print("Something when wrong")
        team_member_name = self.driver.find_element_by_id(self.team_member_name)
        team_member_name.send_keys("Jova")
        ''' using coordinate somehow not working so i tried to tap element in behind'''
        # x = team_member_name.location['x']
        # y = team_member_name.location['y']
        # height = team_member_name.size['height']
        # width = team_member_name.size['width']
        # time.sleep(2)
        # suggestion_cord = []
        # suggestion_cord.append((x, y+height+40))
        # suggestion_cord.append((x+(int(width/2)), y+height+50))
        # print(suggestion_cord)
        # self.driver.tap(suggestion_cord)
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/title").click()

    def set_project_role(self):
        self.driver.find_element_by_id(self.project_role).send_keys("Tester")

    def tap_add_member_button(self):
        self.driver.find_element_by_id(self.add_team_member_button).click()

