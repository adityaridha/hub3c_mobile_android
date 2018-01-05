from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import datetime
import pytz
import time

from util import utility


raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]

class CreateNewProject(Page):


    form_title = (By.XPATH, "//*[@text='New Project: Overview']")
    project_name = (By.ID, "au.geekseat.com.hub3candroid:id/edit_project_name")
    project_code = (By.ID, "au.geekseat.com.hub3candroid:id/edit_project_code")
    project_desc = (By.ID, "au.geekseat.com.hub3candroid:id/edit_description")
    currency = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_currency")
    status = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_status")
    proposed_start = (By.ID, "au.geekseat.com.hub3candroid:id/edit_proposed_start")
    proposed_end = (By.ID, "au.geekseat.com.hub3candroid:id/edit_proposed_end")
    actual_start = (By.ID, "au.geekseat.com.hub3candroid:id/edit_actual_start")
    date_completed = (By.ID, "au.geekseat.com.hub3candroid:id/edit_date_complete")

    date_picker_day = (By.ID, "au.geekseat.com.hub3candroid:id/date_picker_day")
    day_today = "//*[@contentDescription='06 October 2017 selected']"

    reminder_date = (By.ID, "au.geekseat.com.hub3candroid:id/edit_reminder_date")
    billing_type = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_billing_type")

    next = (By.ID, "au.geekseat.com.hub3candroid:id/ms_stepNextButton")

    ''' team member section '''

    team_member_sec_title = (By.XPATH, "//*[@text='New Project: Add Member']")
    team_member_name = (By.ID, "au.geekseat.com.hub3candroid:id/add_team_member")
    project_role = (By.ID, "au.geekseat.com.hub3candroid:id/edit_project_role")
    hourly_rate_charge = (By.ID, "au.geekseat.com.hub3candroid:id/edit_hourly_charge")
    hourly_rate_cost = (By.ID, "au.geekseat.com.hub3candroid:id/edit_hourly_cost")
    is_project_owner = (By.ID, "au.geekseat.com.hub3candroid:id/check_owner")
    add_team_member_button = (By.ID, "au.geekseat.com.hub3candroid:id/button_save")
    team_member_hourly_validation = (By.ID, "android:id/message")

    project_creator_option = (By.XPATH, "//*[@resource-id='au.geekseat.com.hub3candroid:id/ib_action_more' and ./parent::*[@class='android.widget.RelativeLayout'] and ./preceding-sibling::*[./*[./*[./*[@text='John Doe']]]]]")

    # //*[@resource-id='au.geekseat.com.hub3candroid:id/ib_action_more' and ./parent::*[@class='android.widget.RelativeLayout'] and ./preceding-sibling::*[./*[./*[./*[@text='John Doe']]]]]
    # (//*[@id='rv_team_project']/*/*[@id='ib_action_more'])[1]

    yes_button = (By.ID, "android:id/button1")
    no_button = (By.ID, "android:id/button2")
    popup_edit = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")

    ''' activity section '''

    add_activity_title = (By.XPATH, "//*[@text='New Project: Add Activities']")
    activity_subject = (By.ID, "au.geekseat.com.hub3candroid:id/et_subject")
    activity_description = (By.ID, "au.geekseat.com.hub3candroid:id/et_description")
    activity_type = (By.ID, "au.geekseat.com.hub3candroid:id/spinner_activity_type")
    schedule_start = (By.ID, "au.geekseat.com.hub3candroid:id/et_date_start")
    is_billable = (By.ID, "au.geekseat.com.hub3candroid:id/switch_is_billable")
    complete_button = (By.ID, "au.geekseat.com.hub3candroid:id/ms_stepCompleteButton")
    save_activity = (By.ID, "au.geekseat.com.hub3candroid:id/btn_add")
    cancel = (By.ID, "au.geekseat.com.hub3candroid:id/btn_cancel")
    activity_validation = (By.ID, "android:id/message")

    def __init__(self):
        super().__init__()
        self.util = utility.StepHelper(self.driver)

    def verified_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.form_title))
            WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(self.project_name))
            print("Create project is Ready")
        except TimeoutException:
            print("Create project not ready")

    def input_project_title(self):
        self.driver.find_element(self.project_name).send_keys("Appium Project {}".format(date))

    def input_project_code(self):
        self.driver.find_element(self.project_code).send_keys("Ap12")

    def input_project_desc(self):
        self.driver.find_element(self.project_desc).send_keys("This project is from automation")

    def set_reminder_date(self):
        self.driver.find_element(self.reminder_date).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click() #harus diganti locator nya

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def tap_next(self):
        print("next")
        self.driver.find_element(self.next).click()

    def tap_complete(self):
        try:
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(self.complete_button))
            print("Complete button detected")
        except TimeoutException:
            print("no complete button")

        self.driver.find_element(self.complete_button).click()
        print("tap complete")


    def handle_team_member_validation(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.team_member_hourly_validation))
            print("hourly rate warning")
        except TimeoutException:
            print("No hourly rate warning")

        self.driver.find_element(self.yes_button).click()

    def handle_activity_validation(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.team_member_hourly_validation))
            self.driver.find_element(self.yes_button).click()
        except TimeoutException:
            print("No hourly rate warning")

    def input_team_member_name(self, teamm_ember_name):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.team_member_sec_title))
            print("Add team member page is ready")
        except TimeoutException:
            print("Team member page not ready")
        team_member_name_el = self.driver.find_element(self.team_member_name)
        team_member_name_el.send_keys(teamm_ember_name)
        self.tap_first_result_auto_complete(team_member_name_el)
        # self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/title").click()

    def set_project_role(self):
        self.driver.find_element(self.project_role).send_keys("Tester")

    def set_hourly_rate(self):
        charge = self.driver.find_element(self.hourly_rate_charge)
        charge.clear()
        charge.send_keys("999")
        cost = self.driver.find_element(self.hourly_rate_cost)
        cost.clear()
        cost.send_keys("999")

    def tap_option_team_member(self):
        # try:
        #     WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.project_creator_option)))
        # except TimeoutException:
        #     print("more option can't be located")

        self.driver.find_element_by_xpath(self.project_creator_option).click()

    def tap_popup_edit(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.popup_edit))
        except TimeoutException:
            print("pop up not appear")

        self.driver.find_element(self.popup_edit).click()

    def tap_add_member_button(self):
        self.driver.find_element(self.add_team_member_button).click()
        time.sleep(2)

    def input_activity_subject(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.add_activity_title))
        except TimeoutException:
            print("activity section is not ready")

        self.driver.find_element(self.activity_subject).send_keys("Activty 1")

    def input_activity_description(self):
        self.driver.find_element(self.activity_description).send_keys("Activity Description")

    def select_activity_type(self):
        activity_type = self.driver.find_element(self.activity_type)
        activity_type.click()
        self.tap_first_result_auto_complete(activity_type)
        time.sleep(1)

    def set_schedule_start(self):
        self.driver.find_element(self.schedule_start).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click()
        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def set_is_billible(self):
        self.driver.find_element(self.is_billable).click()

    def tap_save_activity(self):
        self.driver.find_element(self.save_activity).click()

    def set_is_project_owner(self):
        self.driver.find_element(self.is_project_owner).click()






