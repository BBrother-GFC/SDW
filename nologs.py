import subprocess
import sys
import logging
import os

# 检查是否存在 logs.txt 文件，如果存在则删除它
log_file = '/root/main/logs.txt'
if os.path.exists(log_file):
    os.remove(log_file)

# 配置日志
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 创建一个将输出同时发送到控制台和日志文件的处理程序
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# 重定向标准输出和标准错误到日志文件和控制台
sys.stdout = logging.getLogger().handlers[0].stream
sys.stderr = logging.getLogger().handlers[0].stream

try:
    # 在try块中运行v2_3.py，并将输出重定向到日志文件
    print ("开始运行安装文件...")
    with open(log_file, 'a') as log_file_handle:
        subprocess.run(['python', 'BuShu.py'], check=True, stdout=log_file_handle, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    # 捕获异常并记录到日志文件
    logging.exception(f"程序发生异常: {e}")
except Exception as e:
    # 捕获其他异常并记录到日志文件
    logging.exception(f"程序发生异常: {e}")
finally:
    print ("安装完毕！")
    # 最后，关闭日志处理程序，以确保所有日志都被写入到日志文件
    logging.getLogger().removeHandler(console_handler)
    console_handler.close()
