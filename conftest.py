import os
import sys
import pytest
from pathlib import Path
root = Path(__file__).parents[0]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
print(sys.path)
from connection import Connection

parent_directory = os.getcwd()
failed_screenshot_dir = parent_directory + "\\screenshot\\failed_test\\"
success_screenshot_dir = parent_directory + "\\screenshot\\success_test\\"

driver = Connection.driver

@pytest.fixture()
def reset_app():
    os.system("adb shell pm clear au.geekseat.com.hub3candroid")

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            file_name = file_name.replace("/","_")
            driver.get_screenshot_as_file(failed_screenshot_dir+file_name)
