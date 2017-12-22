from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
from util import StepHelper
import pytest
import time


class ProjectDetail():

    overview_label = (By.XPATH, "//*[@text='OVERVIEW']")
    activities_label = (By.XPATH, "//*[@text='ACTIVITIES']")
    team_members_label = (By.XPATH, "//*[@text='TEAM MEMBERS']")
    bulletin_label = (By.XPATH, "//*[@text='PROJECT BULLETIN']")
    notes_label = (By.XPATH, "//*[@text='NOTES']")
    attachment_label = (By.XPATH, "//*[@text='ATTACHMENT']")
    agenda_label = (By.XPATH, "//*[@text='AGENDA']")
    timesheet_label = (By.XPATH, "//*[@text='TIMESHEET']")

    def __init__(self, driver):
        self.driver = driver
        self.step_helper = StepHelper(driver)

    def go_to_attachment(self):
        self.step_helper.find_element(self.activities_label).click()
        self.step_helper.find_element(self.team_members_label).click()
        self.step_helper.find_element(self.bulletin_label).click()
        self.step_helper.find_element(self.notes_label).click()
        self.step_helper.find_element(self.attachment_label).click()

    def go_to_activities(self):
        self.step_helper.find_element(self.activities_label).click()

    def go_to_team_member(self):
        self.step_helper.find_element(self.activities_label).click()
        self.step_helper.find_element(self.team_members_label).click()

    def go_to_bulletin(self):
        self.step_helper.find_element(self.activities_label).click()
        self.step_helper.find_element(self.team_members_label).click()
        self.step_helper.find_element(self.bulletin_label).click()

    def go_to_notes(self):
        self.step_helper.find_element(self.activities_label).click()
        self.step_helper.find_element(self.team_members_label).click()
        self.step_helper.find_element(self.bulletin_label).click()
        self.step_helper.find_element(self.notes_label).click()








