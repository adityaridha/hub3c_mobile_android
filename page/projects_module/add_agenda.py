from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class AddAgenda():
    agenda_subject = "au.geekseat.com.hub3candroid:id/edit_title"
    agenda_description = "au.geekseat.com.hub3candroid:id/edit_description"
    agenda_date = "au.geekseat.com.hub3candroid:id/edit_date"
    agenda_time = "au.geekseat.com.hub3candroid:id/edit_time"
    add_agenda_button = "au.geekseat.com.hub3candroid:id/button_save"