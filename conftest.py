import pytest
from selenium import webdriver
from data import Urls
from selenium.webdriver.firefox.options import Options 


# фикстура для запуска тестов в браузере Firefox

@pytest.fixture(params=["firefox"])
def driver(request):
     # Создаем объект Options для Firefox
    firefox_options = Options()
    
    # Добавляем аргумент --headless
    firefox_options.add_argument("--headless")
    
    # Можно добавить другие полезные опции, например, для логирования
    # firefox_options.log.level = "trace" # Для отладки
    
    # Передаем настроенные опции при создании драйвера
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()