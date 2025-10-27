import random
from typing import Optional, Literal
from pages.base_page import BasePage


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

    def input_firstname(self, firstname: str):
        self.driver.find_element(*self._FIRST_NAME_FIELD).send_keys(firstname)

    def input_lastname(self, lastname: str):
        self.driver.find_element(*self._LAST_NAME_FIELD).send_keys(lastname)

    def input_email(self, email: str):
        self.driver.find_element(*self._EMAIL_FIELD).send_keys(email)

    def input_email_re(self, email: str):
        self.driver.find_element(*self._REPEAT_EMAIL_FIELD).send_keys(email)

    def input_username(self, username: str):
        self.driver.find_element(*self._USERNAME_FIELD).send_keys(username)

    def input_password(self, password: str):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    def click_birthdate(self):
        self.driver.find_element(*self._BIRTHDATE_FIELD).click()

    def select_current_birthdate(self):
        self.driver.find_element(*self._CURRENT_DAY_FIELD).click()

    def select_sex(self, gender: Literal['male', 'female'] = 'male'):
        select_sex = None
        if gender:
            select_sex = self._MALE_SEX_RBTN if gender == 'male' else self._FEMALE_SEX_RBTN
        else:
            ValueError("Another gender does not exist")
        self.driver.find_element(*select_sex).click()

    def check_gdpr_agree(self):
        self.driver.find_element(*self._GDPR_CHECKBOX).click()

    def click_create_account(self):
        self.driver.find_element(*self._CREATE_BTN).click()

    def assert_positve_message_about_creation(self):
        msg = self.driver.find_element(*self._CREATE_ACCOUNT_MESSAGE_POSITIVE)
        assert msg.is_displayed()
        assert "Your account has been registered!" in msg.text