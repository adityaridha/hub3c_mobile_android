from connection import Connection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest

con = Connection()


class Page(object):

    app_package = con.capabilities['appPackage']
    _driver = con.driver()

    def __init__(self):
        pass

    @property
    def driver(self):
        print("restart ?")
        return self._driver

    def find_element(self, element, time_out=10):
        try:
            result = WebDriverWait(self.driver, time_out).until(ec.presence_of_element_located(element))
            return result
        except TimeoutException:
            print("This element couldn't be found : {} ".format(element))
            pytest.fail()


if __name__ == "__main__" :
    pass
