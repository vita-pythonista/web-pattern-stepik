from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"

    _USERNAME_FIELD = "[name='username']"
    _PASSWORD_FIELD = "[name='password']"
    _LOGIN_BTN = ".btn[value='Login']"

    def input_username(self, username: str):
        self.clear(self._USERNAME_FIELD)
        self.enter_text(self._USERNAME_FIELD, username)

    def input_password(self, password: str):
        self.clear(self._PASSWORD_FIELD)
        self.enter_text(self._PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self._LOGIN_BTN)