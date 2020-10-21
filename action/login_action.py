from common.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By


class LoginAction(BasePage):
    login_click=(By.XPATH,u'//*[@id="u1"]/a')
    login_exchange=(By.XPATH,u'//*[@id="TANGRAM__PSP_11__footerULoginBtn"]')
    login_username=(By.NAME,u"userName")
    login_password=(By.NAME,u"password")
    login_enter=(By.ID,u"TANGRAM__PSP_11__submit")

    username='luojingnihao2'
    password='q907740164'


    def login_click_action(self):
        self.locator(*self.login_click).click()

    def login_exchange_action(self):
        #self.page.login_exchange.click()
        self.locator(*self.login_exchange).click()

    def login_username_action(self,username1):
        #self.page.login_username='luojingnihao2'
        self.locator(*self.login_username).send_keys(username1)

    def login_password_action(self,password1):
        #self.page.login_password='q907740164'
        self.locator(*self.login_password).send_keys(password1)

    def login_enter_action(self):
        #self.page.login_enter.click()
        self.locator(*self.login_enter).click()

    def login(self):
        self.open()
        sleep(2)
        self.login_click_action()
        sleep(2)
        self.login_exchange_action()
        sleep(2)
        self.login_username_action(self.username)
        self.login_password_action(self.password)
        sleep(1)
        self.login_enter_action()
        sleep(2)
