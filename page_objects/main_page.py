import allure
from page_objects.base_page import *
from locators.main_page_locators import *
from data import *

class MainPage(BasePage):

# кнопка "Оставить заявку" 
    @allure.step('Кликнуть по кнопке "Оставить заявку" в хэдере')
    def click_button_submit_application(self):
        self.wait_for_element(MainPageLocators.header_button_submit_application)
        self.wait_for_element_click(MainPageLocators.header_button_submit_application)
        self.click_on_element(MainPageLocators.header_button_submit_application)

    @allure.step('Проверить отображение формы "Свяжитесь с нами"')
    def check_visibility_section_contact(self):
        self.wait_for_element(MainPageLocators.contact_us_title)
        contact_section = self.find_element_with_wait(MainPageLocators.contact_us_title)
        return self.driver.execute_script(JS.script, contact_section) 

# кнопка "Узнать больше"
    @allure.step('Кликнуть по кнопке "Узнать больше" в хэдере')
    def click_on_button_learn_more(self):
        self.wait_for_element(MainPageLocators.header_button_learn_more)
        self.wait_for_element_click(MainPageLocators.header_button_learn_more)
        self.click_on_element(MainPageLocators.header_button_learn_more)

    @allure.step('Проверить отображение формы "Форматы сотрудничества"')
    def check_visibility_section_cooperation_formats(self):
        self.wait_for_element(MainPageLocators.cooperation_formats_title)
        cooperation_formats_section = self.find_element_with_wait(MainPageLocators.cooperation_formats_title)
        return self.driver.execute_script(JS.script, cooperation_formats_section)    

# кнопка "Актуальные вакансии"
    @allure.step('Кликнуть по кнопке "Актуальные вакансии" в хэдере')
    def click_on_button_current_vacancies(self):
        self.wait_for_element(MainPageLocators.header_button_current_vacancies)
        self.wait_for_element_click(MainPageLocators.header_button_current_vacancies)
        self.click_on_element(MainPageLocators.header_button_current_vacancies)

    @allure.step('Переключиться на вкладку вакансий')
    def switch_window_vacancies(self):
        self.switch_window()

    @allure.step('Получение URL страницы с вакансиями')
    def get_url_page_vacancies(self):
        actual_url = self.get_page_url()
        return actual_url
    
# кнопкa 'Выбрать формат' в в форме 'Аутстафф'
    @allure.step("Скролл до кнопки 'Выбрать формат' в в форме 'Аутстафф'")
    def scroll_button_choose_format_form_outstaff(self):
        self.scroll_to_element(MainPageLocators.button_choose_format_form_outstaff)    
    
    @allure.step('Кликнуть по кнопке "Выбрать формат" в форме "Аутстафф"')
    def click_on_button_choose_format_form_outstaff(self):
        self.wait_for_element(MainPageLocators.button_choose_format_form_outstaff)
        self.wait_for_element_click(MainPageLocators.button_choose_format_form_outstaff)
        self.click_on_element(MainPageLocators.button_choose_format_form_outstaff)

# кнопкa 'Выбрать формат' в в форме 'Помощь в трудоустройстве'
    @allure.step("Скролл до кнопки 'Выбрать формат' в в форме 'Помощь в трудоустройстве'")
    def scroll_button_choose_format_form_help_employment(self):
        self.scroll_to_element(MainPageLocators.button_choose_format_form_help_employment)    
    
    @allure.step('Кликнуть по кнопке "Выбрать формат" в форме "Помощь в трудоустройстве"')
    def click_on_button_choose_format_form_help_employment(self):
        self.wait_for_element(MainPageLocators.button_choose_format_form_help_employment)
        self.wait_for_element_click(MainPageLocators.button_choose_format_form_help_employment)
        self.click_on_element(MainPageLocators.button_choose_format_form_help_employment)

# кнопка 'О нас' в футере
    @allure.step("Скролл до кнопки 'О нас' в футере")
    def scroll_button_about_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_about)    
    
    @allure.step('Кликнуть по кнопке " О нас " в футере')
    def click_on_button_about_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_about)
        self.wait_for_element_click(MainPageLocators.footer_button_about)
        self.click_on_element(MainPageLocators.footer_button_about)   

    @allure.step('Проверить отображение окна "O компании"')
    def check_visibility_section_about(self):
        self.wait_for_element(MainPageLocators.title_about_company)
        about_section = self.find_element_with_wait(MainPageLocators.title_about_company)
        return self.driver.execute_script(JS.script, about_section)
    
# кнопка 'Вакансии' в футере
    @allure.step("Скролл до кнопки 'О нас' в футере")
    def scroll_button_vacancy_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_vacancy)

    @allure.step('Кликнуть по кнопке " Вакансии " в футере')
    def click_on_button_vacancy_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_vacancy)
        self.wait_for_element_click(MainPageLocators.footer_button_vacancy)
        self.click_on_element(MainPageLocators.footer_button_vacancy) 

    @allure.step('Проверить отображение окна "Кого мы ищем"')
    def check_visibility_section_vacancy(self):
        self.wait_for_element(MainPageLocators.title_vacancy)
        vacancy_section = self.find_element_with_wait(MainPageLocators.title_vacancy)
        return self.driver.execute_script(JS.script, vacancy_section) 
    
# кнопка 'Отзывы' в футере
    @allure.step("Скролл до кнопки 'О нас' в футере")
    def scroll_button_reviews_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_reviews)

    @allure.step('Кликнуть по кнопке "Отзывы" в футере')
    def click_on_button_reviews_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_reviews)
        self.wait_for_element_click(MainPageLocators.footer_button_reviews)
        self.click_on_element(MainPageLocators.footer_button_reviews) 

    @allure.step('Проверить отображение окна "Отзывы специалистов"')
    def check_visibility_section_reviews(self):
        self.wait_for_element(MainPageLocators.title_reviews)
        reviews_section = self.find_element_with_wait(MainPageLocators.title_reviews)
        return self.driver.execute_script(JS.script, reviews_section) 

# кнопка 'Контакты' в футере
    @allure.step("Скролл до кнопки 'Контакты' в футере")
    def scroll_button_contact_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_contact)  

    @allure.step('Кликнуть по кнопке "Контакты" в футере')
    def click_on_button_contact_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_contact)
        self.wait_for_element_click(MainPageLocators.footer_button_contact)
        self.click_on_element(MainPageLocators.footer_button_contact)  

    @allure.step('Проверить отображение окна "Связаться с нами"')
    def check_visibility_section_contact(self):
        self.wait_for_element(MainPageLocators.contact_us_title)
        contact_section = self.find_element_with_wait(MainPageLocators.contact_us_title)
        return self.driver.execute_script(JS.script, contact_section)  

# кнопка 'Аутстафф' в футере
    @allure.step("Скролл до кнопки 'Аутстафф' в футере")
    def scroll_button_outstaff_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_outstaff)  

    @allure.step('Кликнуть по кнопке "Аутстафф" в футере')
    def click_on_button_outstaff_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_outstaff)
        self.wait_for_element_click(MainPageLocators.footer_button_outstaff)
        self.click_on_element(MainPageLocators.footer_button_outstaff)     

# кнопка 'Трудоустройство' в футере
    @allure.step("Скролл до кнопки 'Трудоустройство' в футере")
    def scroll_button_employment_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_employment)  

    @allure.step('Кликнуть по кнопке "Трудоустройство" в футере')
    def click_on_button_employment_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_employment)
        self.wait_for_element_click(MainPageLocators.footer_button_employment)
        self.click_on_element(MainPageLocators.footer_button_employment)  

# кнопка 'Консультация' в футере
    @allure.step("Скролл до кнопки 'Трудоустройство' в футере")
    def scroll_button_consultation_footer(self):
        self.scroll_to_element(MainPageLocators.footer_button_consultation)  

    @allure.step('Кликнуть по кнопке "Консультация" в футере')
    def click_on_button_consultation_footer(self):
        self.wait_for_element(MainPageLocators.footer_button_consultation)
        self.wait_for_element_click(MainPageLocators.footer_button_consultation)
        self.click_on_element(MainPageLocators.footer_button_consultation)    
    
# получение адреса страницы после клика с якорем    
    @allure.step('Получение URL страницы после клика')
    def get_url_page_anchor(self):
        actual_url = self.get_page_url()
        return actual_url

    


    
    
