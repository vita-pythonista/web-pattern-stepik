import random
from typing import Optional, Literal
from pages.base_page import BasePage


class RegistationPage(BasePage):

    PAGE_URL = 'https://demo.opensource-socialnetwork.org'

    FIRST_NAME_FIELD = ("css selector", "input[name='firstname']")
    LAST_NAME_FIELD = ("css selector", "input[name='lastname']")
    EMAIL_FIELD = ("css selector", "input[name='email']")
    REPEAT_EMAIL_FIELD = ("css selector", "input[name='email_re']")
    USERNAME_FIELD = ("css selector", "input[name='username']")
    PASSWORD_FIELD = ("css selector", "input[name='password']")
    BIRTHDATE_FIELD = ("css selector", "input[name='birthdate']")
    CURRENT_DAY_FIELD = ("css selector", "td.ui-datepicker-today")
    MALE_SEX_RBTN = ("css selector", "[name='gender'][value='male']")
    FEMALE_SEX_RBTN = ("css selector", "[name='gender'][value='female']")
    GDPR_CHECKBOX = ("css selector", "input[name='gdpr_agree']")
    CREATE_BTN = ("css selector", "input[value='Create an account']")
    CREATE_ACCOUNT_MESSAGE_POSITIVE = ("css selector", "div.ossn-message-done")

    def input_firstname(self, firstname: str):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(firstname)

    def input_lastname(self, lastname: str):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(lastname)

    def input_email(self, email: str):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def input_email_re(self, email: str):
        self.driver.find_element(*self.REPEAT_EMAIL_FIELD).send_keys(email)

    def input_username(self, username: str):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def input_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_birthdate(self):
        self.driver.find_element(*self.BIRTHDATE_FIELD).click()

    def select_current_birthdate(self):
        self.driver.find_element(*self.CURRENT_DAY_FIELD).click()

    def select_sex(self, gender: Literal['male', 'female'] = 'male'):
        select_sex = None
        if gender:
            select_sex = self.MALE_SEX_RBTN if gender == 'male' else self.FEMALE_SEX_RBTN
        else:
            ValueError("Another gender does not exist")
        self.driver.find_element(*select_sex).click()

    def check_gdpr_agree(self):
        self.driver.find_element(*self.GDPR_CHECKBOX).click()

    def click_create_account(self):
        self.driver.find_element(*self.CREATE_BTN).click()

    def assert_positve_message_about_creation(self):
        msg = self.driver.find_element(*self.CREATE_ACCOUNT_MESSAGE_POSITIVE)
        assert msg.is_displayed()
        assert "Your account has been registered!" in msg.text