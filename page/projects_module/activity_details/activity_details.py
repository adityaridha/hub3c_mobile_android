from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class ActivityDetails():

    activity_name = (By.ID, "au.geekseat.com.hub3candroid:id/text_name")
    edit_activity = (By.ID, "au.geekseat.com.hub3candroid:id/tv_edit")
    activity_assignee = (By.ID, "au.geekseat.com.hub3candroid:id/text_assigned")
    activity_status = (By.ID, "au.geekseat.com.hub3candroid:id/text_status")
    activity_progress = (By.ID, "au.geekseat.com.hub3candroid:id/tv_progress")
    activity_progress_bar = (By.ID, "au.geekseat.com.hub3candroid:id/progressBar")

    '''diagnostic'''
    proposed_start = (By.ID, "au.geekseat.com.hub3candroid:id/text_proposed_start")
    actual_start = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_start")
    proposed_due = (By.ID, "au.geekseat.com.hub3candroid:id/text_proposed_due")
    actual_due = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_due")
    reminder_date = (By.ID, "au.geekseat.com.hub3candroid:id/text_proposed_reminder")
    budget_days = (By.ID, "au.geekseat.com.hub3candroid:id/text_budget_activity_days")
    actual_days = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_activity_days")
    budget_time = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_activity_days") #KAYAKNYA SALAH
    actual_time = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_time")
    budget_cost = (By.ID, "au.geekseat.com.hub3candroid:id/text_budget_cost")
    actual_cost = (By.ID, "au.geekseat.com.hub3candroid:id/text_actual_cost")