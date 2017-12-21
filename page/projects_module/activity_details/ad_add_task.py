from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class AddTask():
    task_subject = "au.geekseat.com.hub3candroid:id/et_subject"
    task_predecessor = "au.geekseat.com.hub3candroid:id/edit_predecessors"
    task_type = "au.geekseat.com.hub3candroid:id/spinner_activity_type"
    task_description = "au.geekseat.com.hub3candroid:id/et_description"
    task_budget = "au.geekseat.com.hub3candroid:id/et_activity_budget"
    task_budget_hours = "au.geekseat.com.hub3candroid:id/et_activity_hours"
    task_sequence = "au.geekseat.com.hub3candroid:id/spinner_sequence"
    task_assignee = "au.geekseat.com.hub3candroid:id/spinner_assigned_to"
    task_status = "au.geekseat.com.hub3candroid:id/spinner_status"
    task_status_update = "au.geekseat.com.hub3candroid:id/et_status_update"
    task_progress_bar = "au.geekseat.com.hub3candroid:id/seek_progress"
    task_progress = "au.geekseat.com.hub3candroid:id/tv_progress"
    task_priority = "au.geekseat.com.hub3candroid:id/spinner_priority"
    task_proposed_start_date = "au.geekseat.com.hub3candroid:id/et_date_start"
    task_proposed_start_time = "au.geekseat.com.hub3candroid:id/et_time_start"
    task_proposed_finish_date = "au.geekseat.com.hub3candroid:id/et_date_finish"
    task_proposed_finish_time = "au.geekseat.com.hub3candroid:id/et_time_finish"
    task_actual_start_date = "au.geekseat.com.hub3candroid:id/et_date_actual_start"
    task_actual_start_time = "au.geekseat.com.hub3candroid:id/et_time_actual_start"
    task_actual_finish_date = "au.geekseat.com.hub3candroid:id/et_date_completed"
    task_actual_finish_time = "au.geekseat.com.hub3candroid:id/et_time_completed"
    task_reminder_date = "au.geekseat.com.hub3candroid:id/et_date_reminder"
    task_reminder_time = "au.geekseat.com.hub3candroid:id/et_time_reminder"
    task_mark_completed = "au.geekseat.com.hub3candroid:id/switch_marks_as_complete"
    task_as_billable = "au.geekseat.com.hub3candroid:id/switch_is_billable"
    add_task_button = "au.geekseat.com.hub3candroid:id/btn_add"
