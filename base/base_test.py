from pages.registation_page import RegistationPage
from pages.login_page import LoginPage
from pages.home_page.home_page import HomePage
from data.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.data = Credentials()
        self.registation_page = lambda driver=self.driver: RegistationPage(driver)
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.home_page = lambda driver=self.driver: HomePage(driver)