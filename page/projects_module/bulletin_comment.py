from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time
import pytest
from util import utility


raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]

class BulletinComment():

    bulletin = ""
    bulletin_like_button = ""
    bulletin_like_count = ""
    comment_poster = ""
    comment_poster_picture = ""
    comment_like_button = ""
    comment_like_count = ""