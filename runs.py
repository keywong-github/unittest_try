import unittest
import time
from common.Write_Report import Write_Report1
from common.Send_Email import Send_Email1

if __name__=='__main__':
    test_dir='./test_case'
    suit=unittest.defaultTestLoader.discover(test_dir,'test*.py')

    html_report=Write_Report1().write_report(suit)
    #发邮件开关
    # Send_Email1().send_mail(html_report)








    #send_mail(html_report)
    # fp=open(html_report,'wb')
    # runner=HTMLTestRunner(stream=fp,description='这是描述部分')
    # runner.run(suit,rerun=0,save_last_run=False)
    # fp.close()

    # runner=BeautifulReport(suit)
    # runner.report(filename=html_report,description='美化版邮件发送')


