import allure
import pytest

"""
Удалены импорты классов страниц
Фикстура page не передается в теста 
Фикстуры login_page и dashboard_page используются для инициализации соответствующих объектов.
Тесты становятся более лаконичными и легко читаемыми.
"""
@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure(login_page): # login_page из фикстуры conftest.py
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()  # переход на страницу авторизации
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')  # и заполнение полей логина и пароля с неверными учетными данными
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'  # проверка

@allure.feature('Авторизация')
@allure.story('Авторизация действительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password): # login_page и dashboard_page из фикстуры conftest.py
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()  # переход на страницу авторизации
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)  # и заполнение полей логина и пароля
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")  # Проверяется, что на странице отображается корректное приветственное сообщение.
