# -*- coding:utf-8 -*-
import logging
import os

https://www.cnblogs.com/hanmk/p/10448963.html

log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(log_path)
#d:\2020\vscode\mine\my-autotest
class Logger:
    
    def __init__(self,loggername):

        #创建一个logger
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，用于写入日志文件
        log_path1 = log_path +'/log/'
        # print(log_path1)
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把logs变成文件名的一部分了
        logname = log_path1 + 'out.log' #指定输出的日志文件名
        fh = logging.FileHandler(logname,encoding = 'utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        fh.setLevel(logging.DEBUG)

        #创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s name:[%(name)s] level:[%(levelname)s]   ---%(message)s',"%Y-%m-%d-%X")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def get_log(self):

        return self.logger


if __name__ == '__main__':
    t = Logger("hmk").get_log().debug("User %s is loging" % 'jeck')