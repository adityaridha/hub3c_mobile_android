from connection import Connection
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pytest



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


if __name__ == "__main__" :
    pass
