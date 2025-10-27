import time

from base.base_test import BaseTest


class TestPost(BaseTest):

    def test_publish_post(self):
        self.login_page.open()
        self.login_page.input_username("administrator")
        self.login_page.input_password("administrator")
        self.login_page.click_login_button()
        time.sleep(3)