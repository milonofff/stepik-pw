# project/pages/dashboard_page.py
from playwright.sync_api import Page, expect


# project/pages/dashboard_page.py
class DashboardPage:
    def __init__(self, page: Page):
        self.page = page # сохраняет ссылку на объект страницы для использования в методах класса.
        self.profile = page.locator('#usernameDisplay') # инициализируют локаторы для элементов страницы
        self.logout = page.locator('#logout') # инициализируют локаторы для элементов страницы


    def assert_welcome_message(self, message): #  проверяет текст приветственного сообщения на панели управления.
        expect(self.profile).to_have_text(message)