from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
import time


class EditProject():

    el_project_name_id = "au.geekseat.com.hub3candroid:id/edit_project_name"
    el_project_code_id = "au.geekseat.com.hub3candroid:id/edit_project_code"
    el_project_description_id = "au.geekseat.com.hub3candroid:id/edit_description"
    el_currency_id = "au.geekseat.com.hub3candroid:id/spinner_currency"
    el_project_status_id = "au.geekseat.com.hub3candroid:id/spinner_status"
    el_proposed_start_id = "au.geekseat.com.hub3candroid:id/edit_proposed_start"
    el_proposed_end_id = "au.geekseat.com.hub3candroid:id/edit_proposed_end"
    el_actial_start_id = "au.geekseat.com.hub3candroid:id/edit_actual_start"
    el_date_completed_id = "au.geekseat.com.hub3candroid:id/edit_date_complete"
    el_reminder_date_id = "au.geekseat.com.hub3candroid:id/edit_reminder_date"
    el_billing_type_id = "au.geekseat.com.hub3candroid:id/spinner_billing_type"
    el_fixed_price_amount_id = "au.geekseat.com.hub3candroid:id/input_fixed_amount"
    el_save_buton_id = "au.geekseat.com.hub3candroid:id/btn_add"
    el_cancel_button_id = "au.geekseat.com.hub3candroid:id/btn_add"

    def __init__(self, driver):
        self.driver = driver

    def edit_project_name(self):
        pass

    def edit_project_code(self):
        pass

    def edit_project_description(self):
        pass

    def edit_currency(self):
        pass

    def edit_project_status(self):
        pass

    def edit_proposed_start(self):
        pass

    def edit_proposed_end(self):
        pass

    def edit_actual_start(self):
        pass

    def edit_date_completed(self):
        pass

    def edit_reminder_date(self):
        pass

    def edit_billing_type(self):
        pass

    def edit_fixed_price_amount(self):
        pass

    def save_edit_project(self):
        pass

    def tap_cancel_button(self):
        pass




