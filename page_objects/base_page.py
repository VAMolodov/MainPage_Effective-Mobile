import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator, timeout=10)
        element.click()
    

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)
    
    @allure.step('Переключение между вкладками')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить адрес страницы')
    def get_page_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание смены URL с 'about:blank'")
    def wait_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))
    
    @allure.step("Подождать видимости элемента в DOM")
    def wait_for_element_DOM(self, locator,timeout=10):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))
    
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element_DOM(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Подождать кликабельности  элемента")
    def wait_for_element_click(self, locator,timeout=10):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))