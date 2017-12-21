from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class AddActivity():
    activity_parent = "au.geekseat.com.hub3candroid:id/spinner_parent_activity"
    activity_predecessor = "au.geekseat.com.hub3candroid:id/edit_predecessors"
    activity_subject = "au.geekseat.com.hub3candroid:id/et_subject"
    activity_type = "au.geekseat.com.hub3candroid:id/spinner_activity_type"
    activity_description = "au.geekseat.com.hub3candroid:id/et_description"
    activity_budget = "au.geekseat.com.hub3candroid:id/et_activity_budget"
    activity_budget_hours = "au.geekseat.com.hub3candroid:id/et_activity_hours"
    activity_sequence = "au.geekseat.com.hub3candroid:id/spinner_sequence"
    activity_assignee = "au.geekseat.com.hub3candroid:id/spinner_assigned_to"
    activity_status = "au.geekseat.com.hub3candroid:id/spinner_status"
    activity_status_update = "au.geekseat.com.hub3candroid:id/et_status_update"
    activity_progress_bar = "au.geekseat.com.hub3candroid:id/seek_progress"
    activity_progress = "au.geekseat.com.hub3candroid:id/tv_progress"
    activity_priority = "au.geekseat.com.hub3candroid:id/spinner_priority"
    activity_proposed_start_date = "au.geekseat.com.hub3candroid:id/et_date_start"
    activity_proposed_start_time = "au.geekseat.com.hub3candroid:id/et_time_start"
    activity_proposed_finish_date = "au.geekseat.com.hub3candroid:id/et_date_finish"
    activity_proposed_finish_time = "au.geekseat.com.hub3candroid:id/et_time_finish"
    activity_actual_start_date = "au.geekseat.com.hub3candroid:id/et_date_actual_start"
    activity_actual_start_time = "au.geekseat.com.hub3candroid:id/et_time_actual_start"
    activity_actual_finish_date = "au.geekseat.com.hub3candroid:id/et_date_completed"
    activity_actual_finish_time = "au.geekseat.com.hub3candroid:id/et_time_completed"
    activity_reminder_date = "au.geekseat.com.hub3candroid:id/et_date_reminder"
    activity_reminder_time = "au.geekseat.com.hub3candroid:id/et_time_reminder"
    activity_mark_completed = "au.geekseat.com.hub3candroid:id/switch_marks_as_complete"
    activity_as_billable = "au.geekseat.com.hub3candroid:id/switch_is_billable"
    add_activity_button = "au.geekseat.com.hub3candroid:id/btn_add"
