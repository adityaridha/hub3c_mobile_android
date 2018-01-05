from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility
from page.base_page import Page

raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]


class ActivityNotes():

    notes_textbox = (By.ID, "au.geekseat.com.hub3candroid:id/edit_input_note")
    notes_save_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_save_note")
    search_textfield = (By.ID, "android:id/search_src_text")
    notes_poster = (By.ID, "au.geekseat.com.hub3candroid:id/tv_name")
    notes_you = (By.ID, "au.geekseat.com.hub3candroid:id/tv_is_that_you")
    notes_poster_picture = "(//*[@id='rv_notes_project']/*/*/*[@class='android.widget.ImageView' and @width>0 and @height>0 and ./following-sibling::*[./*[@id='tv_name']]])[1]"
    notes_time = (By.ID, "au.geekseat.com.hub3candroid:id/tv_time")
    notes_title = (By.ID, "au.geekseat.com.hub3candroid:id/tv_subject_note")
    notes_content = (By.ID, "au.geekseat.com.hub3candroid:id/tv_note")
    notes_edit_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")
    load_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_view_all")
    success_message = (By.XPATH, "")

    ''' edit notes '''

    edit_notes_textbox = (By.ID, "au.geekseat.com.hub3candroid:id/et_file_name")
    edit_notes_cancel = (By.XPATH, "//*[@id='button2']")
    edit_notes_save= (By.XPATH, "//*[@id='button1']")
    success_message_edit = (By.XPATH, "")

    '''ADD NOTES'''

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.notes_textbox))
            print("Add notes is ready")
        except TimeoutException:
            print("Add notes is not ready")

    def input_notes(self):
        self.driver.find_element(self.notes_textbox).send_keys("Automated Notes{}".format(date))

    def tap_save_notes(self):
        self.driver.find_element(self.notes_save_button).click()

    def verify_notes(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.presence_of_all_elements_located(self.success_message))
            print("Add Notes is successful")
        except TimeoutException:
            print("Add Notes is unsuccessful")
            pytest.fail()

    '''EDIT NOTES'''

    def tap_edit_button(self):
        self.driver.find_element(self.notes_edit_button).click()

    def edit_notes(self):
        self.driver.find_element(self.edit_notes_textbox).send_keys("Automated Edit Notes()".format(date))

    def save_edit_notes(self):
        self.driver.find_element(self.edit_notes_save).click()

    def verify_edit_notes(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.presence_of_all_elements_located(self.success_message_edit))
            print("Edit Notes is successful")
        except TimeoutException:
            print("Edit Notes is unsuccessful")
            pytest.fail()