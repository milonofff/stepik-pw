from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page # сохраняет ссылку на объект страницы для использования в методах класса.
        self.username_input = page.locator('#username') # Поле ввода имени пользователя
        self.password_input = page.locator('#password') # Поле ввода пароля
        self.login_button = page.locator('#login') # Кнопка входа
        self.error_message = page.locator('#errorAlert') # Сообщение об ошибке

    def navigate(self): # Этот метод открывает страницу логина. Он использует метод goto из Playwright для перехода по URL.
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):  # Этот метод выполняет вход с заданными учетными данными.
                                                    # Он заполняет поля имени пользователя и пароля и нажимает кнопку входа
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self): # Этот метод возвращает текст сообщения об ошибке, если вход не удался.
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()