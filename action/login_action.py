from common.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By


class LoginAction(BasePage):
    login_click=(By.XPATH,'//*[@id="u1"]/a')
    login_exchange=(By.XPATH,'//*[@id="TANGRAM__PSP_11__footerULoginBtn"]')
    login_username=(By.NAME,"userName")
    login_password=(By.NAME,"password")
    login_enter=(By.ID,"TANGRAM__PSP_11__submit")


    def login_click_action(self,*login_click):
        self.locator(login_click).click()

    def login_exchange_action(self,*login_exchange):
        #self.page.login_exchange.click()
        self.locator(*login_exchange).click()

    def login_username_action(self,*login_username):
        #self.page.login_username='luojingnihao2'
        self.locator(*login_username).send_keys('luojingnihao2')

    def login_password_action(self,*login_password):
        #self.page.login_password='q907740164'
        self.locator(*login_password).send_keys('q907740164')

    def login_enter_action(self,*login_enter):
        #self.page.login_enter.click()
        self.locator(*login_enter).click()

    def login(self):
        self.open()
        self.login_click_action()
        sleep(2)
        self.login_exchange_action()
        sleep(2)
        self.login_username_action()
        self.login_password_action()
        sleep(1)
        self.login_enter_action()
        sleep(2)
