import sys
import os
import time
from pathlib import Path
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

parent_directory = os.getcwd()
failed_screenshot_dir = parent_directory + "\\test_screenshot\\failed_screenshot\\"
success_screenshot_dir = parent_directory + "\\test_screenshot\\success_screenshot\\"

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class StepHelper:

    def __init__(self, driver):
        self.driver = driver

    def get_failed_screenshot(self, test_name):
        self.driver.save_screenshot(failed_screenshot_dir + "{}-{}.png".format(now, test_name))

    def get_screenshot(self, test_name):
        self.driver.save_screenshot(success_screenshot_dir + "{}-{}.png".format(now, test_name))

    def find_element(self, element, time_out=10):

        try:
            result = WebDriverWait(self.driver, time_out).until(ec.presence_of_element_located(element))
            return result
        except TimeoutException:
            print("This element couldn't be found : {} ".format(element))
            pytest.fail()

    def swipe_to_buttom(self):
        time.sleep(1)
        try:
            self.driver.swipe(522, 800, 495, 100, 1000)
            print("swipe success")
        except :
            print("swipe failed")









