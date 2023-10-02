# -*- coding: utf-8 -*-

import binascii
import os
import subprocess
import wget
import fileinput
import requests
import datetime
import re

# 初始化变量
a = ""
b = ""
c = ""
d = ""
D = ""
w = ""
st = ""
ca = ""
t = ""

# 打开并执行txt文件
with open('BianLiang.txt', 'r') as file:
    code = file.read()

# 去除每行开头和结尾的空格、空行等
cleaned_code = '\n'.join(line.strip() for line in code.splitlines() if line.strip())

# 执行干净的代码
exec(cleaned_code)

# 使用subprocess运行git clone命令
def run_git_clone(repo_url, destination):
    subprocess.run(["git", "clone", repo_url, destination])

extensions_path = "/content/stable-diffusion-webui/extensions"

extensions_to_clone = [
    (f"https://github.com/camenduru/stable-diffusion-webui-huggingface", f"{extensions_path}/stable-diffusion-webui-huggingface"),
    (f"https://github.com/hnmr293/posex", f"{extensions_path}/posex"),
    (f"https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN", f"{extensions_path}/stable-diffusion-webui-localization-zh_CN"),
    (f"https://github.com/hanamizuki-ai/stable-diffusion-webui-localization-zh_Hans", f"/extensions/stable-diffusion-webui-localization-zh_Hans"),
    (f"https://github.com/zanllp/sd-webui-infinite-image-browsing", f"{extensions_path}/sd-webui-infinite-image-browsing"),
    (f"https://github.com/Physton/sd-webui-prompt-all-in-one", f"{extensions_path}/sd-webui-prompt-all-in-one"),
    (f"https://github.com/journey-ad/sd-webui-bilingual-localization", f"{extensions_path}/sd-webui-bilingual-localization"),
    (f"https://github.com/Bobo-1125/sd-webui-oldsix-prompt-dynamic", f"{extensions_path}/sd-webui-oldsix-prompt-dynamic"),
    (f"https://github.com/adieyal/sd-dynamic-prompts", f"{extensions_path}/sd-dynamic-prompts"),

    
]

for repo_url, destination in extensions_to_clone:
    run_git_clone(repo_url, destination)


# 定义一个函数来运行wget命令
def run_wget(url, output_path):
    wget_command = ["wget", url, "-O", output_path]
    subprocess.run(wget_command, check=True)

# 定义一个函数来创建文件夹（如果不存在的话）
def create_directory(directory):
    mkdir_command = ["mkdir", "-p", directory]
    subprocess.run(mkdir_command, check=True)
    
