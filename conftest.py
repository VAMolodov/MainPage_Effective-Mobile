import pytest
from selenium import webdriver
from data import Urls


# фикстура для запуска тестов в браузере Firefox

@pytest.fixture(params=["firefox"])
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()