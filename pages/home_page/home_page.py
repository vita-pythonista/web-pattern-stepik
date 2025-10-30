import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from pages.home_page.components.post_block import PostBlock


class HomePage(BasePage):

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

    def __init__(self, driver):
        super().__init__(driver)
        self.post_block = PostBlock(driver)

    @allure.step("Wait for page loading")
    def wait_load_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains(self._PAGE_URL))
