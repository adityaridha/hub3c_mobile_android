from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time

class AddTeamMember():
    team_member = "au.geekseat.com.hub3candroid:id/edit_team_member"
    role = "au.geekseat.com.hub3candroid:id/edit_project_role"
    hourly_rate_charge = "au.geekseat.com.hub3candroid:id/edit_hourly_charge"
    hourly_rate_cost = "au.geekseat.com.hub3candroid:id/edit_hourly_cost"
    save_button = "au.geekseat.com.hub3candroid:id/button_save"