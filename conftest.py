import pytest
import faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

f = faker.Faker()


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
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