
class Urls:
    url_main = 'https://www.effective-mobile.ru' # адрес главной страницы
    url_vacancies = 'https://ai-hunt.ru/vacancies/' # адрес страницы сайта вакансий 

class AnchorsLinks:
    anchors_link_about ='https://www.effective-mobile.ru/#about'
    anchors_link_vacancy ='https://www.effective-mobile.ru/#specializations'
    anchors_link_reviews = 'https://www.effective-mobile.ru/#testimonials'
    anchors_link_contact = 'https://www.effective-mobile.ru/#contact'
    anchors_link_outstaff_and_employment = 'https://www.effective-mobile.ru/#services'

class JS:
    # получения координат элемента относительно окна просмотра
    script = """
    var rect = arguments[0].getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
    """