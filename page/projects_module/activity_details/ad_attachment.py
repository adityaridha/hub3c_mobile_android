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


class ActivityAttachment():
    attachment_name = (By.ID, "au.geekseat.com.hub3candroid:id/tv_name_file")
    attachment_picture = (By.ID, "au.geekseat.com.hub3candroid:id/riv_thumbnail")
    attachment_uploader = (By.ID, "au.geekseat.com.hub3candroid:id/tv_name")
    attachment_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/ib_action_more")
    add_attachment_button = (By.ID, "au.geekseat.com.hub3candroid:id/fab")
    load_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_view_all")

    '''option more button'''
    more_attachment_name = (By.ID, "au.geekseat.com.hub3candroid:id/text_tittle")
    attachment_download = (By.ID, "au.geekseat.com.hub3candroid:id/btn_download")
    attachment_edit = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")
    attachment_delete = (By.ID, "au.geekseat.com.hub3candroid:id/btn_delete")

    '''recent attachement '''
    recent_file = (By.XPATH, "//*[@resource-id='android:id/list']/android.widget.LinearLayout[1]")

    '''permission pop up'''
    permission_pop_up = (By.ID, "com.android.packageinstaller:id/permission_message")
    allow_button = (By.ID, "com.android.packageinstaller:id/permission_allow_button")

    '''attachment'''
    first_file = (By.ID, "android:id/title")

    '''delete confirmation'''
    ok_button = (By.XPATH, "//*[@text='Ok']")
    cancel_button = (By.XPATH, "//*[@text='Cancel']")
    allert_box = (By.ID, "au.geekseat.com.hub3candroid:id/alertTitle")

    '''messages'''
    crouton = (By.XPATH,
               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView")
    successfully_upload_attachment = (By.XPATH, "//*[@text='Attachment successfully uploaded!']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.step_helper = StepHelper(driver)

    def verify_attachment_page_element(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.add_attachment_button))
            print("Attachment page is ready")
        except TimeoutException:
            print("Attachment page is not ready, some element is not found")

    def tap_add_attachment_button(self):
        self.step_helper.find_element(self.add_attachment_button).click()

        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.permission_pop_up))
            self.step_helper.find_element(self.allow_button).click()
            print("handle permission pop up")
        except TimeoutException:
            print("No permission pop up appear")

    def tap_recent_file(self):
        print("select recent file")
        self.step_helper.find_element(self.recent_file).click()
        time.sleep(1)

    def tap_file_to_be_upload(self):

        ''' for geting all attachment candidate name'''

        # elements = self.driver.find_elements(By.ID, "android:id/title")
        # print("List attachment available")
        # for element in elements:
        #     print(element.get_attribute("text"))

        file = self.step_helper.find_element(self.first_file)
        file_name = file.get_attribute("text")
        print(file_name)
        file.click()

    def tap_more_button(self):
        self.step_helper.find_element(self.attachment_more_button).click()

    def tap_delete_button(self):
        self.step_helper.find_element(self.attachment_delete).click()

    def proceed_delete_tap_ok(self):
        self.step_helper.find_element(self.ok_button).click()

    def verify_upload_process(self):
        crouton = self.step_helper.find_element(self.crouton, time_out=60)
        messages = crouton.get_attribute("text")
        print(messages)