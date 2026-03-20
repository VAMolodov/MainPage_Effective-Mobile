from page_objects.main_page import *
from selenium.webdriver.support.ui import WebDriverWait
from conftest import *
from data import *
import allure


class TestMainPage:

    @allure.title('Проверка перехода по клику по кнопке  "Оставить заявку"')
    @allure.description('Тест проверяет что при клике по кнопке "Оставить заявку" попадешь на форму "Свяжитесь с нами"')
    def test_click_button_submit_application(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_button_submit_application()
        # Assert
        assert main_page.check_visibility_section_contact()

    @allure.title('Проверка перехода по клику по кнопке  «Узнать больше»')
    @allure.description('Тест проверяет что при клике по кнопке  «Узнать больше» попадешь на форму "Форматы сотрудничества"')
    def test_click_button_learn_more(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_button_learn_more()
        # Assert
        assert main_page.check_visibility_section_cooperation_formats()

    @allure.title('Проверка перехода по клику по кнопке  «Актуальные вакансии»')
    @allure.description('Тест проверяет что при клике по кнопке «Актуальные вакансии» открывается новая вкладка в новом окне другого сайта с вакансиями')
    def test_click_button_current_vacancies(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_button_current_vacancies()
        main_page.switch_window_vacancies()
        main_page.wait_until_not_about_blank()
        # Assert
        assert main_page.get_url_page_vacancies() == Urls.url_vacancies

    @allure.title('Проверка перехода по клику по кнопке  "Выбрать формат" в форме "Аутстафф"')
    @allure.description('Тест проверяет что при клике по кнопке  "Выбрать формат" в форме "Аутстафф" попадешь на форму "Свяжитесь с нами"')
    def test_click_on_button_choose_format_form_outstaff(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_choose_format_form_outstaff()
        main_page.click_on_button_choose_format_form_outstaff()
        # Assert
        assert main_page.check_visibility_section_contact() 

    @allure.title('Проверка перехода по клику по кнопке  "Выбрать формат" в форме "Помощь в трудоустройстве"')
    @allure.description('Тест проверяет что при клике по кнопке  "Выбрать формат" в форме "Помощь в трудоустройстве" попадешь на форму "Свяжитесь с нами"')
    def test_click_on_button_choose_format_form_help_employment (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_choose_format_form_help_employment()
        main_page.click_on_button_choose_format_form_help_employment()
        # Assert
        assert main_page.check_visibility_section_contact()   

    @allure.title('Проверка перехода по клику по кнопке  "О нас" в футере ')
    @allure.description('Тест проверяет что при клике по кнопке  "О нас" в футере попадешь в раздел "О компании" и что текущий URL после клика равен ожидаемому URL с якорем')
    def test_click_on_button_about_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_about_footer()
        main_page.click_on_button_about_footer()
        # Assert
        assert AnchorsLinks.anchors_link_about == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_about() 

    @allure.title('Проверка перехода по клику по кнопке  "Вакансии" в футере ')
    @allure.description('Тест проверяет что при клике по кнопке  "Вакансии" в футере попадешь в раздел "Кого мы ищем" и что текущий URL после клика равен ожидаемому URL с якорем"')
    def test_click_on_button_vacancy_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_vacancy_footer()
        main_page.click_on_button_vacancy_footer()
        # Assert
        assert AnchorsLinks.anchors_link_vacancy == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_vacancy()  

    @allure.title('Проверка перехода по клику по кнопке  "Отзывы" в футере ')
    @allure.description('Тест проверяет что при клике по кнопке  "Отзывы" в футере попадешь в раздел "Отзывы специалистов" и что текущий URL после клика равен ожидаемому URL с якорем"')
    def test_click_on_button_reviews_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_reviews_footer()
        main_page.click_on_button_reviews_footer()
        # Assert
        assert AnchorsLinks.anchors_link_reviews == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_reviews()
    
    @allure.title('Проверка перехода по клику по кнопке  "Контакты" в футере ')
    @allure.description('Тест проверяет что при клике по кнопке  "Контакты" в футере попадешь в раздел "Свяжитесь с нами" и что текущий URL после клика равен ожидаемому URL с якорем')
    def test_click_on_button_contact_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_contact_footer()
        main_page.click_on_button_contact_footer()
        # Assert
        assert AnchorsLinks.anchors_link_contact == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_contact() 

    
    @allure.title('Проверка перехода по клику по кнопке  "Аутстафф" в футере')
    @allure.description('Тест проверяет что при клике по кнопке  "Аутстафф" в футере попадешь в раздел "Форматы сотрудничества" и что текущий URL после клика равен ожидаемому URL с якорем')
    def test_click_on_button_outstaff_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_outstaff_footer()
        main_page.click_on_button_outstaff_footer()
        # Assert
        assert AnchorsLinks.anchors_link_outstaff_and_employment == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_cooperation_formats()


    @allure.title('Проверка перехода по клику по кнопке  "Трудоустройство" в футере')
    @allure.description('Тест проверяет что при клике по кнопке  "Трудоустройство" в футере попадешь в раздел "Форматы сотрудничества" и что текущий URL после клика равен ожидаемому URL с якорем')
    def test_click_on_button_employment_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_employment_footer()
        main_page.click_on_button_employment_footer()
        # Assert
        assert AnchorsLinks.anchors_link_outstaff_and_employment == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_cooperation_formats()
        

    @allure.title('Проверка перехода по клику по кнопке  "Консультация" в футере ')
    @allure.description('Тест проверяет что при клике по кнопке  "Консультация" в футере попадешь в раздел "Свяжитесь с нами" и что текущий URL после клика равен ожидаемому URL с якорем')
    def test_click_on_button_consultation_footer (self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.scroll_button_consultation_footer()
        main_page.click_on_button_consultation_footer()
        # Assert
        assert AnchorsLinks.anchors_link_contact == main_page.get_url_page_anchor()
        assert main_page.check_visibility_section_contact() 