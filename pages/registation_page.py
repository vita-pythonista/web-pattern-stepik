import os
import allure
from datetime import datetime
from typing import Literal
from base.base_page import BasePage


class RegistationPage(BasePage):

    _PAGE_URL = 'https://demo.opensource-socialnetwork.org'

    _FIRST_NAME_FIELD = ("css selector", "input[name='firstname']")
    _LAST_NAME_FIELD = ("css selector", "input[name='lastname']")
    _EMAIL_FIELD = ("css selector", "input[name='email']")
    _REPEAT_EMAIL_FIELD = ("css selector", "input[name='email_re']")
    _USERNAME_FIELD = ("css selector", "input[name='username']")
    _PASSWORD_FIELD = ("css selector", "input[name='password']")
    _BIRTHDATE_FIELD = ("css selector", "input[name='birthdate']")
    _CURRENT_DAY_FIELD = ("css selector", "td.ui-datepicker-today")
    _MALE_SEX_RBTN = ("css selector", "[name='gender'][value='male']")
    _FEMALE_SEX_RBTN = ("css selector", "[name='gender'][value='female']")
    _GDPR_CHECKBOX = ("css selector", "input[name='gdpr_agree']")
    _CREATE_BTN = ("css selector", "input[value='Create an account']")
    _CREATE_ACCOUNT_MESSAGE_POSITIVE = ("css selector", "div.ossn-message-done")

    @allure.step("Input first name")
    def input_firstname(self, firstname: str):
        self.enter_text(self._FIRST_NAME_FIELD, firstname)

    @allure.step("Input last name")
    def input_lastname(self, lastname: str):
        self.enter_text(self._LAST_NAME_FIELD, lastname)

    @allure.step("Input email")
    def input_email(self, email: str):
        self.enter_text(self._EMAIL_FIELD, email)

    @allure.step("Repeat email")
    def input_email_re(self, email: str):
        self.enter_text(self._REPEAT_EMAIL_FIELD, email)

    @allure.step("Input username")
    def input_username(self, username: str):
        self.enter_text(self._USERNAME_FIELD, username)

    @allure.step("Input password")
    def input_password(self, password: str):
        self.enter_text(self._PASSWORD_FIELD, password)

    @allure.step("Click on birthdate")
    def click_birthdate(self):
        self.click(self._BIRTHDATE_FIELD)

    @allure.step("Click on current day")
    def select_current_birthdate(self):
        self.click(self._CURRENT_DAY_FIELD)

    @allure.step("Select sex")
    def select_sex(self, gender: Literal['male', 'female'] = 'male'):
        select_sex = None
        if gender:
            select_sex = self._MALE_SEX_RBTN if gender == 'male' else self._FEMALE_SEX_RBTN
        else:
            ValueError("Another gender does not exist")
        self.click(select_sex)

    @allure.step("Set active agreement with checkbox")
    def check_gdpr_agree(self):
        self.click(self._GDPR_CHECKBOX)

    @allure.step("Click on create account button")
    def click_create_account(self):
        self.click(self._CREATE_BTN)

    def assert_positve_message_about_creation(self):
        msg = self.find_element(self._CREATE_ACCOUNT_MESSAGE_POSITIVE)
        assert msg.is_displayed()
        assert "Your account has been registered!" in msg.text

    def create_screenshot_before_send_request(self):
        time_string = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/{time_string}.png"
        self.driver.save_screenshot(f"screenshots/{time_string}.png")
        with open(screenshot_path, 'rb') as screenshot_file:
            # Прочитаем бинарные данные и прикладываем их к отчету
            data = screenshot_file.read()
            allure.attach(data, name='Screenshot', attachment_type=allure.attachment_type.PNG)
        os.remove(screenshot_path)