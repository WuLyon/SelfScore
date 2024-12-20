import logging
import datetime
from user import User
import config

# 配置logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

# DearDiary类
class DearDiary:

    def __init__(self):
        # 初始化一个默认用户
        # self.user = User()
        self.user = User('0001', 'Lyon')

    def run(self):
        '''
        程序运行的主循环
        '''
        self.welcome()
        is_done = input('Have you do something today? (y/n)')
        if is_done.lower() == 'y':
            self.user.add_op()
        print(self.user)
    
    def welcome(self):
        '''
        程序启动时的问候语
        '''
        print("Welcome to DearDiary, today is a nice day!")
        print(f'{datetime.date.today()}')

def main():
    deardiary = DearDiary()
    deardiary.run()


if __name__ == "__main__":
    main()