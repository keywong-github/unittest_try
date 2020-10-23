import unittest
import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from action.login_action import LoginAction
from ddt import ddt,data,unpack
from selenium import webdriver
from common.ReadData import ReadData1

@ddt
class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.ts.quit()

    @data(*ReadData1().get_excel_data())
    def test_login_baidu(self,data):
        self.ts=LoginAction(self.driver,data['url'])
        self.ts.login()

if __name__=='__main__':
    unittest.main()


#缺少日志，缺少报告，缺少发邮件
