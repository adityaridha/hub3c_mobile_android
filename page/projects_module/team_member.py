from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility


class TeamMember():

    team_member_total = "au.geekseat.com.hub3candroid:id/tv_sum_team"
    team_member_name = "au.geekseat.com.hub3candroid:id/tv_name"
    team_member_picture = "(//*[@id='rv_team_project']/*/*/*/*[@class='android.widget.ImageView' and @width>0 and ./parent::*[./parent::*[@id='layout_main']]])[1]"
    team_member_role = "au.geekseat.com.hub3candroid:id/tv_job"
    team_member_status = "au.geekseat.com.hub3candroid:id/iv_online_status"
    team_member_more_button = "au.geekseat.com.hub3candroid:id/ib_action_more"
    add_team_member = "au.geekseat.com.hub3candroid:id/fab"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' option more button '''
    more_action = "au.geekseat.com.hub3candroid:id/ib_action_more"
    more_name = "au.geekseat.com.hub3candroid:id/text_tittle"
    more_edit = "au.geekseat.com.hub3candroid:id/btn_edit"
    more_delete = "au.geekseat.com.hub3candroid:id/btn_delete"

    '''delete confirmation'''
    delete_confirm = "//*[@text='Are you sure you want remove this team member?']"
    delete_ok = "android:id/button1"
    delete_cancel = "android:id/button2"
    delete_success_text = "//*[@text='Success remove team member']"


    # inisialisasi

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.Helper(driver=self.driver)

    # buka option more

    def tap_option_for_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.more_action)))
        except TimeoutException:
            print("Team Member is not ready")
        self.driver.find_element_by_id(self.more_action).click()

    def tap_edit_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.more_edit)))
        except TimeoutException:
            print("Edit team member is not ready")
        self.driver.find_element_by_id(self.more_edit).click()

    # buat edit perlu file python baru?

    # delete team member

    def tap_delete_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.more_delete)))
        except TimeoutException:
            print("Delete team member is not ready")
        self.driver.find_element_by_id(self.more_delete).click()

    def proceed_delete_action(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,self.delete_confirm)))
            self.driver.find_element_by_id(self.delete_ok).click()
        except TimeoutException:
            print("Delete confirmation does not appear")
            pytest.fail()

    def verify_delete(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.delete_success_text)))
            print("Delete success")
        except TimeoutException:
            print("Delete failed")
            pytest.fail()
