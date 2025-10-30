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

    def find_element(self, locator: tuple | str):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator[0], locator[1]))
        )
        return element

    def find_elements(self, locator: tuple | str):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((locator[0], locator[1]))
        )
        return elements

    def click(self, locator: tuple | str):
        element = self.find_element(locator)
        element.click()

    def scroll_to(self, locator: tuple | str):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def click_mouse(self, locator: tuple | str):
        element = self.find_element(locator)
        action = ActionChains(self.driver).click(element)
        action.perform()

    def hover_mouse(self, locator: tuple | str):
        element = self.find_element(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.pause(1)
        action.perform()

    def clear(self, locator: tuple | str):
        element = self.find_element(locator)
        element.clear()

    def enter_text(self, locator: tuple | str, text: str):
        element = self.find_element(locator)
        element.send_keys(text)