from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import pytest
import time


class ProjectDetail(Page):

    overview_label = (By.XPATH, "//*[@text='OVERVIEW']")
    activities_label = (By.XPATH, "//*[@text='ACTIVITIES']")
    team_members_label = (By.XPATH, "//*[@text='TEAM MEMBERS']")
    bulletin_label = (By.XPATH, "//*[@text='PROJECT BULLETIN']")
    notes_label = (By.XPATH, "//*[@text='NOTES']")
    attachment_label = (By.XPATH, "//*[@text='ATTACHMENT']")
    agenda_label = (By.XPATH, "//*[@text='AGENDA']")
    timesheet_label = (By.XPATH, "//*[@text='TIMESHEET']")

    def __init__(self):
        super().__init__()


    def go_to_activities(self):
        self.find_element(self.activities_label).click()

    def go_to_team_member(self):
        self.go_to_activities()
        self.find_element(self.team_members_label).click()

    def go_to_bulletin(self):
        self.go_to_team_member()
        self.find_element(self.bulletin_label).click()

    def go_to_notes(self):
        self.go_to_bulletin()
        self.find_element(self.notes_label).click()

    def go_to_attachment(self):
        self.go_to_notes()
        self.find_element(self.attachment_label).click()








