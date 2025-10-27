import time
import faker
from pages.registation_page import RegistationPage

f = faker.Faker()

class TestRegistationPage:

    def setup_method(self):
        self.registation_page = RegistationPage(self.driver)
        self.firstname = f.first_name()
        self.lastname = f.last_name()
        self.email = f.email()
        self.username = f.profile()["username"]
        self.password = f.password()

    def test_registration(self):
        self.registation_page.open()
        self.registation_page.input_firstname(firstname=self.firstname)
        self.registation_page.input_lastname(lastname=self.lastname)
        self.registation_page.input_email(email=self.email)
        self.registation_page.input_email_re(email=self.email)
        self.registation_page.input_username(username=self.username)
        self.registation_page.input_password(password=self.password)
        self.registation_page.click_birthdate()
        self.registation_page.select_current_birthdate()
        self.registation_page.select_sex()
        self.registation_page.check_gdpr_agree()
        self.registation_page.click_create_account()
        self.registation_page.driver.implicitly_wait(4.0)
        self.registation_page.assert_positve_message_about_creation()
