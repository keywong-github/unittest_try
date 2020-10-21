import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from page.login_baidu import login_page
from selenium import webdriver

class BasePage(object):
    
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url
        self.page=login_page(driver)


    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def locator(self,*locator):
        el=self.driver.find_element(*locator)
        return el



    def quit(self):
        self.driver.quit()
