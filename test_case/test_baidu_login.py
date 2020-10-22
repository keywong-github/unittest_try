import unittest
import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from action.login_action import LoginAction
from ddt import ddt,data,unpack
from selenium import webdriver

@ddt
class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.ts.quit()

    @data("https://www.baidu.com/")
    def test_login_baidu(self,url):
        self.ts=LoginAction(self.driver,url)
        self.ts.login()

if __name__=='__main__':
    unittest.main()
