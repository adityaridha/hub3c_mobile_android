from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page import Page
import datetime
import pytz
import time


class Activity(Page):

    search_textbox = (By.ID, "android:id/search_src_text")
    activity_title = (By.ID, "au.geekseat.com.hub3candroid:id/text_tittle_activity")
    activity_assignee_name = (By.ID, "au.geekseat.com.hub3candroid:id/tv_name")
    activity_assignee_picture = (By.ID, "au.geekseat.com.hub3candroid:id/thumbnail")
    activity_progress_bar = (By.ID, "au.geekseat.com.hub3candroid:id/materialProgress")
    activity_status = (By.ID, "au.geekseat.com.hub3candroid:id/text_percentage")
    activity_due_date = (By.ID, "au.geekseat.com.hub3candroid:id/text_due_date")
    activity_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/ib_action_more")
    add_activity = (By.ID, "au.geekseat.com.hub3candroid:id/fab")
    load_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_view_all")

    ''' option more button '''
    more_activity_name = (By.ID, "au.geekseat.com.hub3candroid:id/text_tittle")
    more_alert_me = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")
    more_mark_complete = (By.ID, "au.geekseat.com.hub3candroid:id/btn_complete")
    more_delete = (By.ID, "au.geekseat.com.hub3candroid:id/btn_delete")

    def __init__(self):
        super().__init__()

    def tap_add_activity_button(self):
        ''' handle load asignee that take too long'''
        time.sleep(2)
        self.find_element(self.add_activity).click()