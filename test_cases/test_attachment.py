import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import page
from connection import Connection

directory = '%s/' % os.getcwd()


driver = Connection.driver

login = page.Login(driver)
dashboard = page.Dashboard(driver)
navbar = page.Navbar(driver)
feature_menu = page.Feature(driver)
user_profile = page.UserProfile(driver)
switch_account = page.SwitchAccount(driver)
project = page.ProjectList(driver)
project_detail = page.ProjectDetail(driver)
attachment = page.Attachment(driver)


@pytest.mark.usefixtures("reset_app")
class TestAttachment():

    def test_upload_attachment(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.verify_success_access_project()
        project.tap_project_title()
        project_detail.go_to_attachment()
        attachment.verify_attachment_page_element()
        attachment.tap_add_attachment_button()
        attachment.tap_recent_file()
        attachment.tap_file_to_be_upload()
        attachment.verify_upload_process()


    # def test_delete_attachment(self):
    #     login.login(email="transsystem@mailinator.com", password="ZXasqw12")
    #     dashboard.verified_all_element()
    #     navbar.tap_feature_menu()
    #     feature_menu.tap_projects()
    #     project.verify_success_access_project()
    #     project.tap_project_title()
    #     project_detail.go_to_attachment()
    #     attachment.verify_attachment_page_element()
    #     attachment.tap_more_button()
    #     attachment.tap_delete_button()
    #     attachment.proceed_delete_tap_ok()






