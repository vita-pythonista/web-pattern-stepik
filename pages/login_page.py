from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"

    _USERNAME_FIELD = ("css selector", "[name='username']")
    _PASSWORD_FIELD = ("css selector", "[name='password']")
    _LOGIN_BTN = ("css selector", ".btn[value='Login']")

    def input_username(self, username: str):
        self.enter_text(self._USERNAME_FIELD, username)

    def input_password(self, password: str):
        self.enter_text(self._PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self._LOGIN_BTN)