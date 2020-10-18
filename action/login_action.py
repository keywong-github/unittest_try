
from common.base_page import BasePage
from time import sleep

class LoginAction(BasePage):

    def login_click(self):
        self.page.login_click.click()

    def login_exchange(self):
        self.page.login_exchange.click()

    def login_username(self):
        self.page.login_username='luojingnihao2'

    def login_password(self):
        self.page.login_password='q907740164'

    def login_enter(self):
        self.page.login_enter.click()

    def login(self):
        self.open()
        self.login_click()
        sleep(2)
        self.login_exchange()
        sleep(2)
        self.login_username()
        self.login_password()
        sleep(1)
        self.login_enter()
        sleep(2)
