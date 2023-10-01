'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-09-30 13:25:39
LastEditors: BBrother-GFC 3347951573@qq.com
LastEditTime: 2023-10-01 12:34:52
FilePath: \AI绘图配置\SDW\SW_run.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import subprocess
import sys
import logging
import os
import binascii  # 用于将文本转换为十六进制
import re  # 用于正则表达式

from pathlib import Path

# 检查是否存在 logs_run.txt 文件，如果存在则删除它
log_file = '/root/main/logs_run.txt'
if os.path.exists(log_file):
    os.remove(log_file)

# 检查是否存在 url.txt 文件，如果存在则删除它
url_file = '/root/main/url.txt'
if os.path.exists(url_file):
    os.remove(url_file)

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

# 更改当前工作目录为 /root/main
os.chdir('/root/main/')

try:
    # 在 try 块中运行 /root/main/webui.py，并将输出重定向到日志文件
    with open(log_file, 'a') as log_file_handle, open(url_file, 'a') as url_file_handle:
        #'--skip-torch-cuda-test', '--xformers', '--enable-insecure-extension-access', '--gradio-queue', '--disable-nan-check', '--no-hashing', '--opt-split-attention', '--disable-safe-unpickle', '--api', '--theme', 'dark', '--disable-console-progressbars', '--administrator', '--upcast-sampling', ' --enable-insecure-extension-access', '--multiple'
        process = subprocess.Popen(['python', '/root/main/webui.py', '--api', '--disable-safe-unpickle', '--enable-insecure-extension-access', '--no-download-sd-model', '--no-half-vae', '--xformers', '--disable-console-progressbars', '--theme', 'dark', '--upcast-sampling', '--device-id=0'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        url_pattern = re.compile(r'https?://\S+')

        for line in process.stdout:
            if "Public" in line or "Application" in line:
                # 将包含 "Public" 或 "Application" 的行转换为十六进制并写入 url.txt
                hex_line = binascii.hexlify(line.encode()).decode()
                url_file_handle.write(hex_line + '\n')
            else:
                # 查找行中的 URL 地址并将匹配的行转换为十六进制后写入 url.txt
                urls = url_pattern.findall(line)
                if urls:
                    for url in urls:
                        hex_url = binascii.hexlify(url.encode()).decode()
                        url_file_handle.write(hex_url + '\n')

                # 将其他行写入日志文件
                log_file_handle.write(line)
                log_file_handle.flush()

        process.wait()

except subprocess.CalledProcessError as e:
    # 捕获异常并记录到日志文件
    logging.exception(f"程序发生异常: {e}")
except Exception as e:
    # 捕获其他异常并记录到日志文件
    logging.exception(f"程序发生异常: {e}")
finally:
    # 最后，关闭日志处理程序，以确保所有日志都被写入到日志文件
    logging.getLogger().removeHandler(console_handler)
    console_handler.close()
