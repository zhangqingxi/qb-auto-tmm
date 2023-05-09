import argparse
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))
from tool.qb import *

qb_name = None

# 解析参数
def args():
    global qb_name
    ARGP = argparse.ArgumentParser(
        description='这是一个自动化种子管理',
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    ARGP.add_argument('-h', '--help', action='help', help='这是提示信息')
    ARGP.add_argument('-n', '--qb_name', required=True, help='下载器的名称. .env文件配置的前缀名称')

    argp = ARGP.parse_args()
    qb_name = argp.qb_name

    # 加载env文件
    load_dotenv(verbose=True)


   
   
    

if __name__ == '__main__':
    args()
    
    if qb_name == '1':
        name = "Jane Austens Mafia 1998 The Crew 2000 1080p Blu-ray AVC DTS-HD MA 2.0"

        groups = os.getenv('CHDBITS_HR_GROUP').split(',')
        
        
        print(groups)
        exit(1)

    
    
    
    qb = Qb(qb_name=qb_name)
    qb.login()

    tries = 1
    if qb.cookie is None and tries <= 5:
        tries = tries + 1
        qb.login()

    if qb.cookie is None:
        print('登录失败，请检查用户信息')
        exit(-1)

    # 处理种子
    qb.get_torrents().handle_torrents().delete_torrent()

    print('Done')
