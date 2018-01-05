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


class Bulletin():

    bulletin_textbox = (By.ID, "au.geekseat.com.hub3candroid:id/edit_input_bulletin")
    bulletin_post_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_save_bulletin")
    bulletin_poster = (By.ID, "au.geekseat.com.hub3candroid:id/tv_user_name")
    bulletin_poster_picture = (By.ID, "au.geekseat.com.hub3candroid:id/riv_thumbnail")
    bulletin_content = (By.ID, "au.geekseat.com.hub3candroid:id/tv_text")
    bulletin_time = (By.ID, "au.geekseat.com.hub3candroid:id/tv_time")
    bulletin_like_button = (By.ID, "au.geekseat.com.hub3candroid:id/iv_like")
    bulletin_like_total = (By.ID, "au.geekseat.com.hub3candroid:id/tv_like")
    bulletin_comment_button = (By.ID, "au.geekseat.com.hub3candroid:id/iv_comment")
    bulletin_comment_total = (By.ID, "au.geekseat.com.hub3candroid:id/tv_comment")
    load_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_view_all")

    '''edit bulletin'''
    bulletin_edit_button = (By.ID, "")
    bulletin_textbox_edit = (By.ID, "au.geekseat.com.hub3candroid:id/edit_text")
    bulletin_save_button = (By.ID, "au.geekseat.com.hub3candroid:id/button_save")
    success_message_edit = (By.ID, "")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def verify_form(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.bulletin_textbox))
            print("Bulletin is ready")
        except TimeoutException:
            print("Bulletin is not ready")

    def tap_like_button(self):
        self.driver.find_element(self.bulletin_like_button).click()

    def tap_comment_button(self):
        self.driver.find_element(self.bulletin_comment_button).click()

    '''EDIT BULLETIN'''

    def tap_edit_button(self):
        self.driver.find_element(self.bulletin_edit_button).click()

    def edit_bulletin(self):
        self.driver.find_element(self.bulletin_textbox_edit).send_keys("Automated Edit Bulletin()".format(date))

    def save_edit_bulletin(self):
        self.driver.find_element(self.bulletin_save_button).click()

    def verify_edit_bulletin(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.presence_of_all_elements_located(self.success_message_edit))
            print("Edit Bulletin is successful")
        except TimeoutException:
            print("Edit Bulletin is unsuccessful")
            pytest.fail()