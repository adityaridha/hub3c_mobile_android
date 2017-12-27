from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import pytest
import time


class SwitchAccount(Page):

    header = "//*[@text='Please select your desired account to be switched:']"

    def __init__(self):
        super().__init__()

    def select_business_nama(self, business):
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, self.header)))
        except TimeoutException:
            print("No multiple business")

        self.driver.find_element_by_xpath("//*[@text='{}']".format(business)).click()