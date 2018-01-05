from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
import pytest


class Calendar(Page):


    current_date = (By.ID, "au.geekseat.com.hub3candroid:id/date_picker_day")
    current_year = (By.ID, "au.geekseat.com.hub3candroid:id/date_picker_year")
    ok_button = (By.ID, "au.geekseat.com.hub3candroid:id/ok")
    cancel_button = (By.ID, "au.geekseat.com.hub3candroid:id/cancel")
    clear_button = (By.ID, "au.geekseat.com.hub3candroid:id/clear")

    def __init__(self):
        super().__init__()

    def select_date(self, mode = "future", index=1):
        '''
        content description attribute is can't be retrieved,
        so current implementation using work arround find by xpath

        '''
        current_date = self.find_element(self.current_date)
        print("current date is {}".format(current_date.text))
        date = current_date.text[-2:]
        current_date.click()

        if mode == "future":
            new_date = int(date) + index
        else:
            new_date = int(date) - index
            print("select date that already passed")

        self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'{}')]".format(new_date)).click()
        self.find_element(self.ok_button).click()




