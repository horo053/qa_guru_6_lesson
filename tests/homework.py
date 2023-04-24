from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if 22 <= current_time.hour or current_time.hour < 6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user == None:
        if 22 <= current_time.hour or current_time.hour < 6:
            is_dark_theme = True
        else:
            is_dark_theme = False
    elif dark_theme_enabled_by_user == True:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = ([key for key in users if key['name'] == 'Olga'][0])
    assert suitable_users == {"name": "Olga", "age": 45}
    #Решение найдено на https://www.delftstack.com/ru/howto/python/python-search-list-of-dictionaries/

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = ([key for key in users if key['age'] < 20])
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

# Решение найдено на https://pythonist.ru/strokovye-metody-split-i-join-v-python/
def print_name_and_argument(func, *args):
    return f'{func.__name__.replace("_", " ").title()} [{", ".join(args)}]'

def open_browser(browser_name):
    actual_result = print_name_and_argument(open_browser, browser_name)
    print(actual_result)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_name_and_argument(go_to_companyname_homepage, page_url)
    print(actual_result)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_name_and_argument(find_registration_button_on_login_page, page_url, button_text)
    print(actual_result)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
