import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class HomePage(BasePage):

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

    _POST_BLOCK = ("css_selector", "#ossn-wall-form")
    _POST_TEXTAREA = ("xpath", "//*[@id='ossn-wall-form']/fieldset/div[2]/textarea")
    _POST_PUBLISH_BTN = ("xpath", "//input[@type='submit']")
    _PUBLISHED_POSTS = ("xpath", "//*[starts-with(@id,'activity-item')]")

    def wait_load_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains(self._PAGE_URL))

    def create_post(self, text: str):
        self.click_mouse(self._POST_TEXTAREA)
        self.enter_text(self._POST_TEXTAREA, text)
        self.click_mouse(self._POST_PUBLISH_BTN)

    def find_published_posts(self):
        elements = self.find_elements(self._PUBLISHED_POSTS)
        return elements