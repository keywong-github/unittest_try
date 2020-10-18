import sys
from os.path import abspath,dirname
sys.path.append(dirname(dirname(abspath(__file__))))
from page.page_sa import PageSa

class BasePage(object):
    def __init__(self,driver,url,username,password):
        self.driver=driver
        self.url=url
        self.username=username
        self.password=password
        self.page=PageSa(driver)

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()