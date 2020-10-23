import time
from BeautifulReport import BeautifulReport
from  HTMLTestRunner import HTMLTestRunner
import unittest

class Write_Report1:
    def write_report(self,suit):
        #调试用
        # test_dir='./test_case'
        # suit1=unittest.defaultTestLoader.discover(test_dir,'test*.py')

        now_date=time.strftime('%Y-%m-%d %H_%M_%S')
        html_report='report/'+now_date+'_report.html'
        #fp=open(html_report,'wb')
        # with open (html_report,'wb') as fp:
        #     runner=HTMLTestRunner(stream=fp,description='这是描述部分')
        #     runner.run(suit)
        #fp.close() with op就不用这个，也可以实现
        runner=BeautifulReport(suit)
        runner.report(filename=html_report,description='美丽的报告')




        return html_report




#Write_Report1().write_report()


