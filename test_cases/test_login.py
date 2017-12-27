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
switch_account = page.SwitchAccount()


@pytest.mark.usefixtures("reset_app")
class TestLogin():

    def test_login_wrong_password(self):
        login.verified_all_element()
        login.input_email("transsystem@mailinator.com")
        login.input_password("this is password")
        login.tap_sign_in()
        login.verify_login_is_failed()

    def test_login_failed3x(self):
        login.verified_all_element()
        login.input_email("transsystem@mailinator.com")
        login.input_password("this is password")
        login.tap_sign_in()
        login.verify_login_is_failed()
        login.input_password("this is password 2")
        login.tap_sign_in()
        login.verify_login_is_failed()
        login.input_password("this is password 3")
        login.tap_sign_in()
        login.verify_login_is_failed()

    def test_login_logout(self):
        login.verified_all_element()
        login.input_email("transsystem@mailinator.com")
        login.input_password("ZXasqw12")
        login.tap_sign_in()
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_header()
        user_profile.tap_logout()
        login.verified_all_element(reset=False)

    def test_login_logout_multiple_business(self):
        login.verified_all_element()
        login.login(email="mobile.testing@mailinator.com", password="ZXasqw12")
        switch_account.select_business_nama(business="Trans System")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_header()
        user_profile.tap_logout()

    # def test_forgot_password(self):
    #     driver.launch_app()
    #     login.tap_forgot_password()
    #     time.sleep(3)
    #
    # def test_registration(self):
    #     driver.launch_app()
    #     login.tap_registration()
    #     time.sleep(2)



