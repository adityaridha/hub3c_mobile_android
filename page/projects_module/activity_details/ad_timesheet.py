from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class ActivityTimesheet():

    timesheet_title = (By.ID, "au.geekseat.com.hub3candroid:id/tv_tittle")
    timesheet_progress_bar = (By.ID, "au.geekseat.com.hub3candroid:id/materialProgress")
    timesheet_progress = (By.ID, "au.geekseat.com.hub3candroid:id/tv_text_progress")
    timesheet_hours_spent = (By.ID, "au.geekseat.com.hub3candroid:id/tv_hour_spent")
    timesheet_budget_hours = (By.ID, "au.geekseat.com.hub3candroid:id/tv_complete_progress")