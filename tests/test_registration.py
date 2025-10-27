from base.base_test import BaseTest


class TestRegistationPage(BaseTest):

    def test_registration(self, fake_user):
        self.registation_page.open()
        self.registation_page.input_firstname(firstname=fake_user['firstname'])
        self.registation_page.input_lastname(lastname=fake_user['lastname'])
        self.registation_page.input_email(email=fake_user['email'])
        self.registation_page.input_email_re(email=fake_user['email'])
        self.registation_page.input_username(username=fake_user['username'])
        self.registation_page.input_password(password=fake_user['password'])
        self.registation_page.click_birthdate()
        self.registation_page.select_current_birthdate()
        self.registation_page.select_sex()
        self.registation_page.check_gdpr_agree()
        self.registation_page.click_create_account()
        self.registation_page.assert_positve_message_about_creation()

