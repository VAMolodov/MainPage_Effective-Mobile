
from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка "Узнать больше" в шапке сайта
    header_button_learn_more = (By.XPATH, '//button[@data-slot="button" and normalize-space(.)="Узнать больше"]')

    # Заголовок раздела "Форматы сотрудничества"
    cooperation_formats_title = (By.XPATH, '//h2[normalize-space(text())="Форматы сотрудничества"]')

    # Кнопка "Актуальные вакансии" в шапке сайта
    header_button_current_vacancies = (By.XPATH, '//a[@data-slot="button" and normalize-space(.)="Актуальные вакансии"]')

    # Кнопка "Оставить заявку" в шапке сайта
    header_button_submit_application = (By.XPATH, '//button[@data-slot="button" and normalize-space(.)="Оставить заявку"]')

    # Заголовок раздела "Свяжитесь с нами"
    contact_us_title = (By.XPATH, '//h2[normalize-space(text())="Свяжитесь с нами"]')

    # Кнопка "Выбрать формат" в форме "Аутстафф"
    button_choose_format_form_outstaff = (By.XPATH, '//div[./h3[text()="Аутстафф"]]/button[@data-slot="button" and text()="Выбрать формат"]')
  
    # Кнопка "Выбрать формат" в форме "Помощь в трудоустройстве"
    button_choose_format_form_help_employment = (By.XPATH, '//div[./h3[text()="Помощь в трудоустройстве"]]/button[@data-slot="button" and text()="Выбрать формат"]')

    # Кнопка "О нас" в футере сайта
    footer_button_about = (By.XPATH, '//a[normalize-space(.)="О нас"]')

    # Заголовок раздела "О компании"
    title_about_company = (By.XPATH, '//h2[normalize-space(text())="О компании"]')

    # Заголовок раздела "Кого мы ищем"
    title_vacancy = (By.XPATH, '//h2[normalize-space(text())="Кого мы ищем"]')

    # Кнопка "Вакансии" в футере сайта
    footer_button_vacancy = (By.XPATH, '//a[normalize-space(.)="Вакансии"]')

    # Кнопка "Отзывы" в футере сайта
    footer_button_reviews = (By.XPATH, '//a[normalize-space(.)="Отзывы"]')

    # Заголовок раздела "Отзывы специалистов"
    title_reviews = (By.XPATH, '//h2[normalize-space(text())="Отзывы специалистов"]')

    # кнопка "Контакты в футере"
    footer_button_contact = (By.XPATH, "//a[normalize-space(.)='Контакты']")

    # кнопка "Аутстафф" в футере
    footer_button_outstaff = (By.XPATH, '//a[normalize-space(.)="Аутстафф"]')

    # кнопка "Трудоустройство" в футере
    footer_button_employment = (By.XPATH, '//a[normalize-space(.)="Трудоустройство"]')

    # кнопка "Консультация" в футере
    footer_button_consultation = (By.XPATH, '//a[normalize-space(.)="Консультация"]')

