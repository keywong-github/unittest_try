import sys
from os.path import abspath,dirname
sys.path.append(dirname(dirname(abspath(__file__))))

from base.BasePage_sa import BasePage
from time import sleep

class login_action1(BasePage):

    # username1="hxming"

    # password1="8888"

    def input_username(self):
        self.page.username_input=self.username

    def input_password(self):
        self.page.password_input=self.password

    def click_button(self):
        self.page.loginin.click()

    def login(self):
        self.open()
        self.input_username()
        self.input_password()
        sleep(2)
        self.click_button()
        # self.quit()