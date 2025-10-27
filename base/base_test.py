from pages.registation_page import RegistationPage
from pages.login_page import LoginPage
from pages.news_feed_page import HomePage


class BaseTest:

    def setup_method(self):
        self.registation_page = RegistationPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)