from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self._PAGE_URL)

    def find_element(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator[0], locator[1]))
        )
        return element

    def click(self, locator: tuple):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.send_keys(text)