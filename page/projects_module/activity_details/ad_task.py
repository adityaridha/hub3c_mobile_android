from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Task():

    task = "//*[@class='android.widget.LinearLayout']"
    task_title = "au.geekseat.com.hub3candroid:id/text_tittle_activity"
    task_assignee_name = "au.geekseat.com.hub3candroid:id/tv_name"
    task_assignee_picture = "au.geekseat.com.hub3candroid:id/thumbnail"
    task_progress_bar = "au.geekseat.com.hub3candroid:id/materialProgress"
    task_due_date = "au.geekseat.com.hub3candroid:id/text_due_date"
    task_status = "au.geekseat.com.hub3candroid:id/text_percentage"
    add_task = "au.geekseat.com.hub3candroid:id/fab"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"