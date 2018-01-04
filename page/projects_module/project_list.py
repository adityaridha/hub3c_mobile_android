from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
from util import StepHelper
import pytest
import time
from page.base_page import Page

'''tambah archive action'''


class ProjectList():

    create_project = (By.ID, "au.geekseat.com.hub3candroid:id/fab")  # generic floating button id
    project_on_top = (By.ID, "au.geekseat.com.hub3candroid:id/title")  # generic project id
    more_action = (By.ID, "au.geekseat.com.hub3candroid:id/ib_action_more")
    start_project = (By.ID, "au.geekseat.com.hub3candroid:id/textStartProject")
    activities_link = (By.ID, "au.geekseat.com.hub3candroid:id/counter")
    search_project = (By.ID, "au.geekseat.com.hub3candroid:id/action_search")
    back_to_dashboard = (By.XPATH, "//*[@contentDescription='Navigate up']")
    team_member_info = (By.XPATH, "(//*[@id='memberContainer']/*[@class='android.widget.ImageView' and @width>0])[1]")
    in_progress_list = (By.XPATH, "//*[@text='IN PROGRESS']" )
    not_yet_started_list = (By.XPATH, "//*[@text='NOT YET STARTED']")
    on_hold_list = (By.XPATH, "//*[@text='ON HOLD']")
    cancelled_list = (By.XPATH, "//*[@text='CANCELLED']")
    completed_list = (By.XPATH, "//*[@text='COMPLETED']")
    archived_list = (By.XPATH, "//*[@text='ARCHIVED']")
    el_edit_project_id = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")
    el_delete_project_id = (By.ID, "au.geekseat.com.hub3candroid:id/btn_delete")
    el_archive_project_id = ""
    el_del_confirmation = (By.XPATH, "//*[@text='Deleting project will remove this project from list and turn off all notification. Do you want to continue?']")
    el_yes_button_for_delete_id = "android:id/button1"
    el_archive_confirmation = ""
    el_yes_button_for_archive = ""
    crouton_successful_delete = (By.XPATH, "//*[@text='Project is successfully deleted']")
    crouton_successful_archive = ""
    project_title = (By.ID, "au.geekseat.com.hub3candroid:id/title")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.step_helper = StepHelper(driver)

    def verify_success_access_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.create_project))
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.in_progress_list))
            print("Success accessing project module")
        except TimeoutException:
            print("Project page is not ready")


    def tap_create_new_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.create_project))
        except TimeoutException:
            print("Create project not ready")
        self.driver.find_element(self.create_project).click()

    def tap_option_for_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.more_action))
        except TimeoutException:
            print("Project not ready")
        self.driver.find_element(self.more_action).click()

    def tap_edit_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.el_edit_project_id))
        except TimeoutException:
            print("Edit project not ready")
        self.driver.find_element(self.el_edit_project_id).click()

    def tap_delete_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.el_delete_project_id))
        except TimeoutException:
            print("Delete project not ready")
        self.driver.find_element(self.el_delete_project_id).click()

    def proceed_delete_action(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(self.el_del_confirmation))
            self.driver.find_element(self.el_yes_button_for_delete_id).click()
        except TimeoutException:
            print("Delete confirmation not appear")
            pytest.fail()

    def verified_delete_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.crouton_successful_delete))
            print("Delete success")
        except TimeoutException:
            print("Delete failed")
            pytest.fail()

    def tap_project_title(self):
        title = self.step_helper.find_element(self.project_title)
        title.click()



    '''ARCHIVE ACTION'''

    def tap_archive_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.el_archive_project_id))
        except TimeoutException:
            print("Archive project not ready")
        self.driver.find_element(self.el_archive_project_id).click()

    def proceed_archive_action(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(self.el_archive_confirmation))
            self.driver.find_element(self.el_yes_button_for_archive).click()
        except TimeoutException:
            print("Archive confirmation not appear")
            pytest.fail()

    def verified_archive_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.crouton_successful_archive))
            print("Archive success")
        except TimeoutException:
            print("Archive failed")
            pytest.fail()



