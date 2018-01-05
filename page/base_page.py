from connection import Connection
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
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
            return None

    def tap_first_result_auto_complete(self, element, index=1):
        x = element.location['x']
        y = element.location['y']
        height = element.size['height']
        width = element.size['width']
        target_x = x + (int(width/2))
        target_y1 = y + height + (30*index)
        target_y2 = y + height + (40*index)

        suggestion_cord = []
        suggestion_cord.append((target_x, target_y1))
        suggestion_cord.append((target_x, target_y2))

        self.driver.tap(suggestion_cord)

    def tap_spinner_options(self, spinner, index=1):
        spinner.click()
        self.tap_first_result_auto_complete(element=spinner, index=index)

    def swipe_to_bottom(self, target_element=None):

        # asus y2 = -100

        if target_element == None :
            try:
                self.driver.swipe(350, 700, 350, 50, 1000)
                print("swipe success")
            except :
                print("swipe failed")

        else:

            print("Swipe to element : {}".format(target_element))

            n = 4
            while n > 0 :
                print("searching...")
                is_element_visible = self.find_element(target_element, time_out=1)
                if is_element_visible == None :
                    self.driver.swipe(350, 700, 350, 50, 1000)
                    n = n - 1
                    # print("swipe count : {} left".format(n))
                else:
                    print("Element found")
                    return

            else:
                print("swipe 4 times but element not found")


if __name__ == "__main__" :
    pass
