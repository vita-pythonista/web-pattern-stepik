import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from metaclass.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        with allure.step(f"Open page: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

    def find_element(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator[0], locator[1]))
        )
        return element

    def find_elements(self, locator: tuple):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((locator[0], locator[1]))
        )
        return elements

    def click(self, locator: tuple):
        element = self.find_element(locator)
        element.click()

    def click_mouse(self, locator: tuple):
        element = self.find_element(locator)
        action = ActionChains(self.driver).click(element)
        action.perform()


    def clear(self, locator: tuple):
        element = self.find_element(locator)
        element.clear()

    def enter_text(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.send_keys(text)
