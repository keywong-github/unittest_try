import logging
import os

class Logger:
    def __init__(self,logname):
        self.logger=logging.getLogger(logname)
        self.logger.setLevel(logging.DEBUG)

        log_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/log/'+'out2.log'

        fh=logging.FileHandler(log_path,encoding='UTF-8')
        fh.setLevel(logging.DEBUG)

        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)

        fomatter=logging.Formatter('%(asctime)s name:[%(name)s] level:[%(levelname)s] : %(message)s ','%Y_%m_%d %X')

        fh.setFormatter(fomatter)
        sh.setFormatter(fomatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def get_logger(self):
        return self.logger

if __name__=="__main__":
    Logger('hyjian').get_logger().debug('测试通过')