import yagmail
import sys
from os.path import abspath,dirname
sys.path.append(dirname(abspath(__file__)))
from config import Config


class Send_Email1:
    def send_mail(self,html_report):
        yag=yagmail.SMTP(user=Config.send_user,password=Config.send_password,host=Config.sent_host)
        #SMTP授权码TFCSSLQAZFPDXPZR/EKHBBRWQYBMZWRCB
        #密码q907740164
        subject=Config.send_subject
        contents=Config.send_contents
        yag.send(Config.accept_user,subject,contents,html_report)