import pytest
import faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

f = faker.Faker()

# создадим функцию для реализации экземпляра драйвера
def get_driver():
    options = webdriver.ChromeOptions()
    # данная опция нужна для разделения на экране
    options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install())
    )
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = get_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def add_users(request):
    user_count = request.param
    drivers = []
    for _ in range(user_count):
        driver = get_driver()
        drivers.append(driver)
    yield drivers
    for driver in drivers:
        driver.quit()


@pytest.fixture
def fake_user():
    firstname = f.first_name()
    lastname = f.last_name()
    email = f.email()
    username = f.profile()["username"]
    password = f.password()
    user = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "username": username,
        "password": password,
    }
    yield user
    del user