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


class Task():

    task = (By.XPATH, "//*[@class='android.widget.LinearLayout']")
    task_title = (By.ID, "au.geekseat.com.hub3candroid:id/text_tittle_activity")
    task_assignee_name = (By.ID, "au.geekseat.com.hub3candroid:id/tv_name")
    task_assignee_picture = (By.ID, "au.geekseat.com.hub3candroid:id/thumbnail")
    task_progress_bar = (By.ID, "au.geekseat.com.hub3candroid:id/materialProgress")
    task_due_date = (By.ID, "au.geekseat.com.hub3candroid:id/text_due_date")
    task_status = (By.ID, "au.geekseat.com.hub3candroid:id/text_percentage")
    add_task = (By.ID, "au.geekseat.com.hub3candroid:id/fab")
    load_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/btn_view_all")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.util = utility.StepHelper(self.driver)

    def tap_add_activity_button(self):
        self.driver.find_element(self.add_task).click()