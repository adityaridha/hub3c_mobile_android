import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import page

directory = '%s/' % os.getcwd()

login = page.Login()
dashboard = page.Dashboard()
navbar = page.Navbar()
feature_menu = page.Feature()
user_profile = page.UserProfile()
project = page.ProjectList()
project_detail = page.ProjectDetail()
activity = page.Activity()
add_activity = page.AddActivity()


@pytest.mark.usefixtures("reset_app")
class TestActivity():

    # def test_add_activity_minimum_req(self):
    #     login.verified_all_element()
    #     login.input_email("transsystem@mailinator.com")
    #     login.input_password("ZXasqw12")
    #     login.tap_sign_in()
    #     dashboard.verified_all_element()
    #     navbar.tap_feature_menu()
    #     feature_menu.tap_projects()
    #     project.verify_success_access_project()
    #     project.tap_project_title()
    #     project_detail.go_to_activities()
    #     activity.tap_add_activity_button()
    #     add_activity.select_type()
    #     add_activity.input_activity_subject("Appium automation")
    #     add_activity.tap_add_activity_button()

    def test_add_activity_all_filled(self):
        login.verified_all_element()
        login.input_email("transsystem@mailinator.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.verify_success_access_project()
        project.tap_project_title()
        project_detail.go_to_activities()
        activity.tap_add_activity_button()
        add_activity.select_type()
        add_activity.input_activity_subject("Appium automation")
        add_activity.input_description()
        add_activity.input_budget()
        add_activity.input_budget_hours()
        add_activity.select_asignee()
        add_activity.set_proposed_finish_date()



