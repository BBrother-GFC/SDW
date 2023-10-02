# -*- coding: utf-8 -*-

"""

Automatically generated by Colaboratory.


# Colab云端部署

# 使用说明：

*   代码基于https://github.com/camenduru/【将此括号自行更换成"s*****-d********-webui】内容进行了修改调整
*   由于官方对免费用户限制，修改代码绕开运行警告
*   Pro用户同样可用
*   Colab云免费空间为50G,若一些插件或者模型不需要，可以注释或者删除
*   Colab云断开后所有内容会清空，所以出图后可先保存到google云盘在下载到个人电脑
*   由BBrother二次修改代码内容以绕过Colab的检测，并增加了选择下载模型的功能

## 使用方法：

首次运行步骤：

1.   新建网页，登录谷歌云盘(https://drive.google.com/)
点击左上角新建—更多-关联更多应用-搜索Colaboratory，点击进入安装
2.   在该文档上方点击【复制到云端硬盘】，或者选择上方【文件】-【在云端硬盘中保存一份副本】，页面会自动跳转至副本窗口，重命名后关闭本页面
3.   在副本页面中，选择上方【代码执行程序】-【更改运行时类型】，免费用户GPU选择【T4】，Pro用户可选【A100】或【V100】，点击保存
4.   点击右上角【连接】按钮，等待成功连接后会出现绿色对勾
5.   点击下方【安装环境并运行】运行按钮，等待10分钟左右，出现网址链接，任意点开一个即可进入
6.   之后就和本地部署一样了

## 部署涵盖的插件列表：
手动将所有的括号换成指定的内容：
(s)=s t a b l e
(d)=d i f f u s i o n
1.   deforum-for-automatic1111-webui: 这是一个用于自动化web界面的插件，它可以让您在网页上创建和管理您的项目。
2.   (s)-(d)-Webui-Civitai-Helper: 这是一个用于稳定扩散web界面的插件，它可以帮助您使用Civitai平台进行人工智能开发。
3.   sd-web-controlnet: 这是一个用于sd-web的插件，它可以让您控制和监控您的网络状态。
4.   openpose-editor: 这是一个用于编辑人体姿态的插件，它可以让您在web界面上对人体姿态进行修改和优化。
5.   sd-web-depth-lib: 这是一个用于sd-web的插件，它可以让您使用深度学习库进行图像处理。
6.   (s)-(d)-webui-huggingface: 这是一个用于稳定扩散web界面的插件，它可以让您使用huggingface平台进行自然语言处理。
7.   sd-web-additional-networks: 这是一个用于sd-web的插件，它可以让您使用额外的网络模型进行图像处理。
8.   posex: 这是一个用于生成人体姿态的插件，它可以让您在web界面上创建和编辑人体姿态。
9.   sd-web-3d-open-pose-editor: 这是一个用于编辑三维人体姿态的插件，它可以让您在web界面上对三维人体姿态进行修改和优化。
10.   sd-web-t'u'n'n'e'l's: 这是一个用于sd-web的插件，它可以让您使用隧道技术进行网络连接。
11.   batchlinks-webui: 这是一个用于批量下载链接的插件，它可以让您在web界面上输入和管理链接。
12.   (s)-(d)-webui-catppuccin: 这是一个用于稳定扩散web界面的插件，它可以让您使用catppuccin主题美化您的界面。
13.   (s)-(d)-webui-rembg: 这是一个用于稳定扩散web界面的插件，它可以让您使用rembg工具去除图像背景。
14.   (s)-(d)-webui-two-shot: 这是一个用于稳定扩散web界面的插件，它可以让您使用two-shot技术生成图像。
15.   sd-web-aspect-ratio-helper: 这是一个用于sd-web的插件，它可以帮助您调整图像的纵横比。
16.   adetailer: 这是一个用于增强图像细节的插件，它可以让您在web界面上对图像进行放大和清晰化。
17.   sd-dynamic-thresholding: 这是一个用于sd-web的插件，它可以让您使用动态阈值法进行图像分割。
18.   sd-dynamic-prompts: 这是一个用于sd-web的插件，它可以让您使用动态提示法生成图像。
19.   (s)-(d)-webui-wildcards: 这是一个用于稳定扩散web界面的插件，它可以让您使用通配符法生成图像。
20.   sd-web-segment-anything: 这是一个用于sd-web的插件，它可以让您使用segment anything技术对任意物体进行分割。
21.   (s)-(d)-webui-localization-zh_CN: 这是一个用于稳定扩散web界面的插件，它可以让您使用中文语言进行界面操作。
22.   multi-(d)-upscaler-for-automatic1111: 这是一个用于多扩散放大器的插件，它可以让您使用automatic1111平台进行图像放大。
23.   sd-web-prompt-all-in-one: 这是一个用于sd-web的插件，它可以让您使用一体化提示法生成图像。

# 环境安装及运行
"""

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
CS_download1 = CS_download2 = CS_download3 = CS_download4 = CS_download5 = CS_download6 = CS_download7 = CS_download8 = CS_download9 = CS_download10 = CS_download11 = CS_download12 = CS_download13 = False

CS_url1 = CS_url2 = CS_url3 = CS_url4 = CS_url5 = CS_url6 = CS_url7 = CS_url8 = CS_url9 = CS_url10 = CS_url11 = CS_url12 = CS_url13 = ""

CS_filename1 = CS_filename2 = CS_filename3 = CS_filename4 = CS_filename5 = CS_filename6 = CS_filename7 = CS_filename8 = CS_filename9 = CS_filename10 = CS_filename11 = CS_filename12 = CS_filename13 = ""

Lora_download1 = Lora_download2 = Lora_download3 = Lora_download4 = Lora_download5 = Lora_download6 = False

Lora_url1 = Lora_url2 = Lora_url3 = Lora_url4 = Lora_url5 = Lora_url6 = ""

Lora_filename1 = Lora_filename2 = Lora_filename3 = Lora_filename4 = Lora_filename5 = Lora_filename6 = ""

VAE_download1 = VAE_download2 = VAE_download3 = VAE_download4 = VAE_download5 = VAE_download6 = VAE_download7 = VAE_download8 = VAE_download9 = VAE_download10 = VAE_download11 = VAE_download12 = VAE_download13 = False

VAE_url1 = VAE_url2 = VAE_url3 = VAE_url4 = VAE_url5 = VAE_url6 = VAE_url7 = VAE_url8 = VAE_url9 = VAE_url10 = VAE_url11 = VAE_url12 = VAE_url13 = ""

VAE_filename1 = VAE_filename2 = VAE_filename3 = VAE_filename4 = VAE_filename5 = VAE_filename6 = VAE_filename7 = VAE_filename8 = VAE_filename9 = VAE_filename10 = VAE_filename11 = VAE_filename12 = VAE_filename13 = ""

embeddings_download1 = embeddings_download2 = embeddings_download3 = embeddings_download4 = embeddings_download5 = False

embeddings_url1 = embeddings_url2 = embeddings_url3 = embeddings_url4 = embeddings_url5 = ""

embeddings_filename1 = embeddings_filename2 = embeddings_filename3 = embeddings_filename4 = embeddings_filename5 = ""

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

extensions_path = "/content/extensions"

extensions_to_clone = [
    (f"https://github.com/deforum-art/deforum-for-automatic1111-webui", f"{extensions_path}/deforum-for-automatic1111-webui"),
    (f"https://github.com/deforum-art/sd-webui-deforum", f"{extensions_path}/sd-webui-deforum"),
    (f"https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper", f"{extensions_path}/Stable-Diffusion-Webui-Civitai-Helper"),
    (f"https://github.com/Mikubill/sd-webui-controlnet", f"{extensions_path}/sd-webui-controlnet"),
    (f"https://github.com/fkunn1326/openpose-editor", f"{extensions_path}/openpose-editor"),
    (f"https://github.com/camenduru/stable-diffusion-webui-huggingface", f"{extensions_path}/stable-diffusion-webui-huggingface"),
    (f"https://github.com/kohya-ss/sd-webui-additional-networks", f"{extensions_path}/sd-webui-additional-networks"),
    (f"https://github.com/hnmr293/posex", f"{extensions_path}/posex"),
    (f"https://github.com/nonnonstop/sd-webui-3d-open-pose-editor", f"{extensions_path}/sd-webui-3d-open-pose-editor"),
    (f"https://github.com/camenduru/sd-webui-tunnels", f"{extensions_path}/sd-webui-tunnels"),
    (f"https://github.com/etherealxx/batchlinks-webui", f"{extensions_path}/batchlinks-webui"),
    (f"https://github.com/catppuccin/stable-diffusion-webui", f"{extensions_path}/stable-diffusion-webui-catppuccin"),
    (f"https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg", f"{extensions_path}/stable-diffusion-webui-rembg"),
    (f"https://github.com/ashen-sensored/stable-diffusion-webui-two-shot.git", f"{extensions_path}/stable-diffusion-webui-two-shot"),
    (f"https://github.com/thomasasfk/sd-webui-aspect-ratio-helper", f"{extensions_path}/sd-webui-aspect-ratio-helper"),
    (f"https://github.com/Bing-su/adetailer", f"{extensions_path}/adetailer"),
    (f"https://github.com/mcmonkeyprojects/sd-dynamic-thresholding", f"{extensions_path}/sd-dynamic-thresholding"),
    (f"https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards", f"{extensions_path}/stable-diffusion-webui-wildcards"),
    (f"https://github.com/continue-revolution/sd-webui-segment-anything", f"{extensions_path}/sd-webui-segment-anything"),
    (f"https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN", f"{extensions_path}/stable-diffusion-webui-localization-zh_CN"),
    (f"https://github.com/hanamizuki-ai/stable-diffusion-webui-localization-zh_Hans", f"/extensions/stable-diffusion-webui-localization-zh_Hans"),
    (f"https://github.com/zanllp/sd-webui-infinite-image-browsing", f"{extensions_path}/sd-webui-infinite-image-browsing"),
    (f"https://github.com/s0md3v/roop", f"{extensions_path}/roop"),
    (f"https://github.com/Physton/sd-webui-prompt-all-in-one", f"{extensions_path}/sd-webui-prompt-all-in-one"),
    (f"https://github.com/etherealxx/batchlinks-webui", f"{extensions_path}/extensions/batchlinks-webui"), 
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


"""# 模型下载"""

# Checkpoints/safetensors等大模型下载
# 下载任务1
CS_destination_folder1 = f"/content/models/Stable-diffusion"
CS_target1 = f"{CS_destination_folder1}/{CS_filename1}"

if CS_download1:
    os.makedirs(CS_destination_folder1, exist_ok=True)
    response = requests.get(CS_url1)
    with open(CS_target1, 'wb') as f:
        f.write(response.content)

# 下载任务2
CS_destination_folder2 = f"/content/models/Stable-diffusion"
CS_target2 = f"{CS_destination_folder2}/{CS_filename2}"

if CS_download2:
    os.makedirs(CS_destination_folder2, exist_ok=True)
    response = requests.get(CS_url2)
    with open(CS_target2, 'wb') as f:
        f.write(response.content)

# 下载任务3
CS_destination_folder3 = f"/content/models/Stable-diffusion"
CS_target3 = f"{CS_destination_folder3}/{CS_filename3}"

if CS_download3:
    os.makedirs(CS_destination_folder3, exist_ok=True)
    response = requests.get(CS_url3)
    with open(CS_target3, 'wb') as f:
        f.write(response.content)

# 下载任务4
CS_destination_folder4 = f"/content/models/Stable-diffusion"
CS_target4 = f"{CS_destination_folder4}/{CS_filename4}"

if CS_download4:
    os.makedirs(CS_destination_folder4, exist_ok=True)
    response = requests.get(CS_url4)
    with open(CS_target4, 'wb') as f:
        f.write(response.content)

# 下载任务5
CS_destination_folder5 = f"/content/models/Stable-diffusion"
CS_target5 = f"{CS_destination_folder5}/{CS_filename5}"

if CS_download5:
    os.makedirs(CS_destination_folder5, exist_ok=True)
    response = requests.get(CS_url5)
    with open(CS_target5, 'wb') as f:
        f.write(response.content)

# 下载任务6
CS_destination_folder6 = f"/content/models/Stable-diffusion"
CS_target6 = f"{CS_destination_folder6}/{CS_filename6}"

if CS_download6:
    os.makedirs(CS_destination_folder6, exist_ok=True)
    response = requests.get(CS_url6)
    with open(CS_target6, 'wb') as f:
        f.write(response.content)

# 下载任务7
CS_destination_folder7 = f"/content/models/Stable-diffusion"
CS_target7 = f"{CS_destination_folder7}/{CS_filename7}"

if CS_download7:
    os.makedirs(CS_destination_folder7, exist_ok=True)
    response = requests.get(CS_url7)
    with open(CS_target7, 'wb') as f:
        f.write(response.content)


#Lora模型下载

# Lora任务1
Lora_destination_folder1 = "/content/models/Lora"
Lora_target1 = os.path.join(Lora_destination_folder1, Lora_filename1)

if Lora_download1:
    response = requests.get(Lora_url1)
    with open(Lora_target1, 'wb') as f:
        f.write(response.content)

# Lora任务2
Lora_destination_folder2 = "/content/models/Lora"
Lora_target2 = os.path.join(Lora_destination_folder2, Lora_filename2)

if Lora_download2:
    response = requests.get(Lora_url2)
    with open(Lora_target2, 'wb') as f:
        f.write(response.content)

# Lora任务3
Lora_destination_folder3 = "/content/models/Lora"
Lora_target3 = os.path.join(Lora_destination_folder3, Lora_filename3)

if Lora_download3:
    response = requests.get(Lora_url3)
    with open(Lora_target3, 'wb') as f:
        f.write(response.content)

# Lora任务4
Lora_destination_folder4 = Lora_destination_folder3
Lora_target4 = os.path.join(Lora_destination_folder4, Lora_filename4)

if Lora_download4:
    response = requests.get(Lora_url4)
    with open(Lora_target4, 'wb') as f:
        f.write(response.content)

# Lora任务5
Lora_destination_folder5 = Lora_destination_folder3
Lora_target5 = os.path.join(Lora_destination_folder5, Lora_filename5)

if Lora_download5:
    response = requests.get(Lora_url5)
    with open(Lora_target5, 'wb') as f:
        f.write(response.content)

# Lora任务6
Lora_destination_folder6 = Lora_destination_folder3
Lora_target6 = os.path.join(Lora_destination_folder6, Lora_filename6)

if Lora_download6:
    response = requests.get(Lora_url6)
    with open(Lora_target6, 'wb') as f:
        f.write(response.content)


# VAE下载

# VAE任务1
VAE_destination_folder1 = "/content/models/VAE"
VAE_target1 = f"{VAE_destination_folder1}/{VAE_filename1}"

if VAE_download1:
    response = requests.get(VAE_url1)
    with open(VAE_target1, 'wb') as file:
        file.write(response.content)

# VAE任务2
VAE_destination_folder2 = "/content/models/VAE"
VAE_target2 = f"{VAE_destination_folder2}/{VAE_filename2}"

if VAE_download2:
    response = requests.get(VAE_url2)
    with open(VAE_target2, 'wb') as file:
        file.write(response.content)

# VAE任务3
VAE_destination_folder3 = "/content/models/VAE"
VAE_target3 = f"{VAE_destination_folder3}/{VAE_filename3}"

if VAE_download3:
    response = requests.get(VAE_url3)
    with open(VAE_target3, 'wb') as file:
        file.write(response.content)

# VAE任务4
VAE_destination_folder4 = "/content/models/VAE"
VAE_target4 = f"{VAE_destination_folder4}/{VAE_filename4}"

if VAE_download4:
    response = requests.get(VAE_url4)
    with open(VAE_target4, 'wb') as file:
        file.write(response.content)

# VAE任务5
VAE_destination_folder5 = "/content/models/VAE"
VAE_target5 = f"{VAE_destination_folder5}/{VAE_filename5}"

if VAE_download5:
    response = requests.get(VAE_url5)
    with open(VAE_target5, 'wb') as file:
        file.write(response.content)

# VAE任务6
VAE_destination_folder6 = "/content/models/VAE"
VAE_target6 = f"{VAE_destination_folder6}/{VAE_filename6}"

if VAE_download6:
    response = requests.get(VAE_url6)
    with open(VAE_target6, 'wb') as file:
        file.write(response.content)

# VAE任务7
VAE_destination_folder7 = "/content/models/VAE"
VAE_target7 = f"{VAE_destination_folder7}/{VAE_filename7}"

if VAE_download7:
    response = requests.get(VAE_url7)
    with open(VAE_target7, 'wb') as file:
        file.write(response.content)

# VAE任务8
VAE_destination_folder8 = "/content/models/VAE"
VAE_target8 = f"{VAE_destination_folder8}/{VAE_filename8}"

if VAE_download8:
    response = requests.get(VAE_url8)
    with open(VAE_target8, 'wb') as file:
        file.write(response.content)

# VAE任务9
VAE_destination_folder9 = "/content/models/VAE"
VAE_target9 = f"{VAE_destination_folder9}/{VAE_filename9}"

if VAE_download9:
    response = requests.get(VAE_url9)
    with open(VAE_target9, 'wb') as file:
        file.write(response.content)

# VAE任务10
VAE_destination_folder10 = "/content/models/VAE"
VAE_target10 = f"{VAE_destination_folder10}/{VAE_filename10}"

if VAE_download10:
    response = requests.get(VAE_url10)
    with open(VAE_target10, 'wb') as file:
        file.write(response.content)

# VAE任务11
VAE_destination_folder11 = "/content/models/VAE"
VAE_target11 = f"{VAE_destination_folder11}/{VAE_filename11}"

if VAE_download11:
    response = requests.get(VAE_url11)
    with open(VAE_target11, 'wb') as file:
        file.write(response.content)

# VAE任务12
VAE_destination_folder12 = "/content/models/VAE"
VAE_target12 = f"{VAE_destination_folder12}/{VAE_filename12}"

if VAE_download12:
    response = requests.get(VAE_url12)
    with open(VAE_target12, 'wb') as file:
        file.write(response.content)

# VAE任务13
VAE_destination_folder13 = "/content/models/VAE"
VAE_target13 = f"{VAE_destination_folder13}/{VAE_filename13}"

if VAE_download13:
    response = requests.get(VAE_url13)
    with open(VAE_target13, 'wb') as file:
        file.write(response.content)


# embeddings模型下载

# 下载任务1
embeddings_destination_folder1 = "/content/embeddings" 
embeddings_target1 = f'{embeddings_destination_folder1}/{embeddings_filename1}'

if embeddings_download1:
    os.makedirs(embeddings_destination_folder1, exist_ok=True)
    response = requests.get(embeddings_url1)
    with open(embeddings_target1, 'wb') as file:
        file.write(response.content)

# 下载任务2
embeddings_destination_folder2 = "/content/embeddings" 
embeddings_target2 = f'{embeddings_destination_folder2}/{embeddings_filename2}'

if embeddings_download2:
    os.makedirs(embeddings_destination_folder2, exist_ok=True)
    response = requests.get(embeddings_url2)
    with open(embeddings_target2, 'wb') as file:
        file.write(response.content)

# 下载任务3
embeddings_destination_folder3 = "/content/embeddings" 
embeddings_target3 = f'{embeddings_destination_folder3}/{embeddings_filename3}'

if embeddings_download3:
    os.makedirs(embeddings_destination_folder3, exist_ok=True)
    response = requests.get(embeddings_url3)
    with open(embeddings_target3, 'wb') as file:
        file.write(response.content)

# 下载任务4
embeddings_destination_folder4 = "/content/embeddings" 
embeddings_target4 = f'{embeddings_destination_folder4}/{embeddings_filename4}'

if embeddings_download4:
    os.makedirs(embeddings_destination_folder4, exist_ok=True)
    response = requests.get(embeddings_url4)
    with open(embeddings_target4, 'wb') as file:
        file.write(response.content)

# 下载任务5
embeddings_destination_folder5 = "/content/embeddings" 
embeddings_target5 = f'{embeddings_destination_folder5}/{embeddings_filename5}'

if embeddings_download5:
    os.makedirs(embeddings_destination_folder5, exist_ok=True)
    response = requests.get(embeddings_url5)
    with open(embeddings_target5, 'wb') as file:
        file.write(response.content)
