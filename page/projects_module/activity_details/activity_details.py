from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class ActivityDetails():

    activity_name = "au.geekseat.com.hub3candroid:id/text_name"
    edit_activity = "au.geekseat.com.hub3candroid:id/tv_edit"
    activity_assignee = "au.geekseat.com.hub3candroid:id/text_assigned"
    activity_status = "au.geekseat.com.hub3candroid:id/text_status"
    activity_progress = "au.geekseat.com.hub3candroid:id/tv_progress"
    activity_progress_bar = "au.geekseat.com.hub3candroid:id/progressBar"

    '''diagnostic'''
    proposed_start = "au.geekseat.com.hub3candroid:id/text_proposed_start"
    actual_start = "au.geekseat.com.hub3candroid:id/text_actual_start"
    proposed_due = "au.geekseat.com.hub3candroid:id/text_proposed_due"
    actual_due = "au.geekseat.com.hub3candroid:id/text_actual_due"
    reminder_date = "au.geekseat.com.hub3candroid:id/text_proposed_reminder"
    budget_days = "au.geekseat.com.hub3candroid:id/text_budget_activity_days"
    actual_days = "au.geekseat.com.hub3candroid:id/text_actual_activity_days"
    budget_time = "au.geekseat.com.hub3candroid:id/text_actual_activity_days"
    actual_time = "au.geekseat.com.hub3candroid:id/text_actual_time"
    budget_cost = "au.geekseat.com.hub3candroid:id/text_budget_cost"
    actual_cost = "au.geekseat.com.hub3candroid:id/text_actual_cost"