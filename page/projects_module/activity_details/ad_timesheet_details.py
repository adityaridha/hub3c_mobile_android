from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class ActivityTimesheetDetails():
    activity_title = (By.ID, "au.geekseat.com.hub3candroid:id/text_tittle")
    activity_assignee = (By.ID, "au.geekseat.com.hub3candroid:id/text_name")
    timesheet_hours = (By.ID, "au.geekseat.com.hub3candroid:id/text_hour")
    timesheet_created_date = (By.ID, "au.geekseat.com.hub3candroid:id/text_date")
    timesheet_more_button = (By.ID, "au.geekseat.com.hub3candroid:id/ib_action_more")


    '''opsi more button'''
    edit_timesheet = (By.ID, "au.geekseat.com.hub3candroid:id/btn_edit")
    delete_timesheet = (By.ID, "au.geekseat.com.hub3candroid:id/btn_delete")