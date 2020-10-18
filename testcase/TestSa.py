import sys
from os.path import abspath,dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import unittest
from selenium import webdriver
from action.login_action import login_action1
from ddt import ddt,data,unpack
from time import sleep

@ddt
class Test_Sa(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        sleep(2)
        self.sp.quit()

    @data(["http://10.2.8.166:9527/sa/","hxming","8888"])
    @unpack
    def test_sa(self,url,loginname,loginpwd):
        self.sp=login_action1(self.driver,url,loginname,loginpwd)
        self.sp.login()

if __name__=='__main__':
    unittest.main()