from pages.registation_page import RegistationPage
from pages.login_page import LoginPage


class BaseTest:

    def setup_method(self):
        self.registation_page = RegistationPage(self.driver)
        self.login_page = LoginPage(self.driver)