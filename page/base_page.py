from connection import Connection
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pytest
import time



class Page(object):

    driver = Connection.driver

    def __init__(self):
        pass

    def find_element(self, element, time_out=10):
        try:
            result = WebDriverWait(self.driver, time_out).until(ec.presence_of_element_located(element))
            return result
        except TimeoutException:
            print("This element couldn't be found : {} ".format(element))
            pytest.fail()

    def tap_first_result_auto_complete(self, element, index=1):
        print(index)
        x = element.location['x']
        y = element.location['y']
        height = element.size['height']
        width = element.size['width']
        target_x = x + (int(width/2))
        target_y1 = y + height + (40*index)
        target_y2 = y + height + (50*index)

        suggestion_cord = []
        suggestion_cord.append((target_x, target_y1))
        suggestion_cord.append((target_x, target_y2))

        self.driver.tap(suggestion_cord)

    def tap_spinner_options(self, spinner, index=1):
        spinner.click()
        self.tap_first_result_auto_complete(element=spinner, index=index)

    def swipe_to_button(self):
        time.sleep(1)
        try:
            self.driver.swipe(522, 800, 495, 100, 1000)
            print("swipe success")
        except :
            print("swipe failed")


if __name__ == "__main__" :
    pass
