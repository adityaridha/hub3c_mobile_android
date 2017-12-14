from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class EditActivityTimesheet():
    team_member = "au.geekseat.com.hub3candroid:id/spinner_team_member"
    activity = "au.geekseat.com.hub3candroid:id/spinner_activity"
    date = "au.geekseat.com.hub3candroid:id/et_date_entered"
    hours_spent = "au.geekseat.com.hub3candroid:id/et_hours_spent"
    remaining_days = "au.geekseat.com.hub3candroid:id/et_days_remaining"
    update_timesheet_button = "au.geekseat.com.hub3candroid:id/btn_add"