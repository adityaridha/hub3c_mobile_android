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


class ActivityNotes():

    notes_textbox = "au.geekseat.com.hub3candroid:id/edit_input_note"
    notes_save_button = "au.geekseat.com.hub3candroid:id/btn_save_note"
    search_textfield = "android:id/search_src_text"
    notes_poster = "au.geekseat.com.hub3candroid:id/tv_name"
    notes_you = "au.geekseat.com.hub3candroid:id/tv_is_that_you"
    notes_poster_picture = "(//*[@id='rv_notes_project']/*/*/*[@class='android.widget.ImageView' and @width>0 and @height>0 and ./following-sibling::*[./*[@id='tv_name']]])[1]"
    notes_time = "au.geekseat.com.hub3candroid:id/tv_time"
    notes_title = "au.geekseat.com.hub3candroid:id/tv_subject_note"
    notes_content = "au.geekseat.com.hub3candroid:id/tv_note"
    notes_edit_button = "au.geekseat.com.hub3candroid:id/btn_edit"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"
    success_message = ""

    ''' edit notes '''

    edit_notes_textbox = "au.geekseat.com.hub3candroid:id/et_file_name"
    edit_notes_cancel = "//*[@id='button2']"
    edit_notes_save= "//*[@id='button1']"
    success_message_edit = ""

    '''ADD NOTES'''

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.notes_textbox)))
            print("Add notes is ready")
        except TimeoutException:
            print("Add notes is not ready")

    def input_notes(self):
        self.driver.find_element_by_id(self.notes_textbox).send_keys("Automated Notes{}".format(date))

    def tap_save_notes(self):
        self.driver.find_element_by_id(self.notes_save_button).click()

    def verify_notes(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located((By.XPATH, self.success_message)))
            print("Add Notes is successful")
        except TimeoutException:
            print("Add Notes is unsuccessful")
            pytest.fail()

    '''EDIT NOTES'''

    def tap_edit_button(self):
        self.driver.find_element_by_id(self.notes_edit_button).click()

    def edit_notes(self):
        self.driver.find_element_by_id(self.edit_notes_textbox).send_keys("Automated Edit Notes()".format(date))

    def save_edit_notes(self):
        self.driver.find_element_by_xpath(self.edit_notes_save).click()

    def verify_edit_notes(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.presence_of_all_elements_located((By.XPATH, self.success_message_edit)))
            print("Edit Notes is successful")
        except TimeoutException:
            print("Edit Notes is unsuccessful")
            pytest.fail()