import time

import allure
import pytest
from base.base_test import BaseTest


@allure.epic("Registration")
@allure.feature("New positive registation")
class TestRegistationPage(BaseTest):

    @allure.story("Check positive registration form")
    def test_registration(self, fake_user):
        self.registation_page().open()
        self.registation_page().input_firstname(firstname=fake_user['firstname'])
        self.registation_page().input_lastname(lastname=fake_user['lastname'])
        self.registation_page().input_email(email=fake_user['email'])
        self.registation_page().input_email_re(email=fake_user['email'])
        self.registation_page().input_username(username=fake_user['username'])
        self.registation_page().input_password(password=fake_user['password'])
        self.registation_page().click_birthdate()
        self.registation_page().select_current_birthdate()
        self.registation_page().select_sex()
        self.registation_page().check_gdpr_agree()
        self.registation_page().create_screenshot_before_send_request()
        self.registation_page().click_create_account()
        self.registation_page().assert_positve_message_about_creation()

    @allure.story("Check positive registration form with 3 users")
    @pytest.mark.parametrize("add_users", [2], indirect=True)
    def test_registration_with_three_users(self, fake_user, add_users):
        user2, user3 = add_users
        self.registation_page().open()
        self.registation_page().input_firstname(firstname=fake_user['firstname'])
        self.registation_page().input_lastname(lastname=fake_user['lastname'])
        time.sleep(2)
        # действия 2-го пользователя
        self.registation_page(user2).open()
        self.registation_page(user2).input_firstname(firstname=fake_user['firstname'])
        self.registation_page(user2).input_lastname(lastname=fake_user['lastname'])
        time.sleep(2)
        # действия 3-го пользователя
        self.registation_page(user3).open()
        self.registation_page(user3).input_firstname(firstname=fake_user['firstname'])
        self.registation_page(user3).input_lastname(lastname=fake_user['lastname'])

