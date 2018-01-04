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


class Bulletin():

    bulletin_textbox = "au.geekseat.com.hub3candroid:id/edit_input_bulletin"
    bulletin_post_button = "au.geekseat.com.hub3candroid:id/btn_save_bulletin"
    bulletin_poster = "au.geekseat.com.hub3candroid:id/tv_user_name"
    bulletin_poster_picture = "au.geekseat.com.hub3candroid:id/riv_thumbnail"
    bulletin_content = "au.geekseat.com.hub3candroid:id/tv_text"
    bulletin_time = "au.geekseat.com.hub3candroid:id/tv_time"
    bulletin_like_button = "au.geekseat.com.hub3candroid:id/iv_like"
    bulletin_like_total = "au.geekseat.com.hub3candroid:id/tv_like"
    bulletin_comment_button = "au.geekseat.com.hub3candroid:id/iv_comment"
    bulletin_comment_total = "au.geekseat.com.hub3candroid:id/tv_comment"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    '''edit bulletin'''
    bulletin_edit_button = ""
    bulletin_textbox_edit = "au.geekseat.com.hub3candroid:id/edit_text"
    bulletin_save_button = "au.geekseat.com.hub3candroid:id/button_save"
    success_message_edit = ""

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.bulletin_textbox)))
            print("Bulletin is ready")
        except TimeoutException:
            print("Bulletin is not ready")

    def tap_like_button(self):
        self.driver.find_element_by_id(self.bulletin_like_button).click()

    def tap_comment_button(self):
        self.driver.find_element_by_id(self.bulletin_comment_button).click()

    '''EDIT BULLETIN'''

    def tap_edit_button(self):
        self.driver.find_element_by_id(self.bulletin_edit_button).click()

    def edit_bulletin(self):
        self.driver.find_element_by_id(self.bulletin_textbox_edit).send_keys("Automated Edit Bulletin()".format(date))

    def save_edit_bulletin(self):
        self.driver.find_element_by_id(self.bulletin_save_button).click()

    def verify_edit_bulletin(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.presence_of_all_elements_located((By.XPATH, self.success_message_edit)))
            print("Edit Bulletin is successful")
        except TimeoutException:
            print("Edit Bulletin is unsuccessful")
            pytest.fail()