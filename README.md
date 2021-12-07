## 使用方法
本项目创建了一个钉钉群机器人，设置两种响应
1、每天早上9:00 发送服务器情况到钉群（包括CPU 负载 存储等数据）
2、时时预警，每30s检测一次（监控负载 CPU使用率情况，超过阀值，钉钉消息报警）

### 下载项目文件
```bash
# ssh下载
git clone git@github.com:XksA-me/DingdingBot.git
# https下载
git clone  https://github.com/XksA-me/DingdingBot.git
# 如果不行可以尝试下面的加速下载地址
# ssh加速地址：git clone git@git.zhlh6.cn:XksA-me/DingdingBot.git
# https加速地址：git clone https://github.com.cnpmjs.org/XksA-me/DingdingBot.git
```

### 安装项目依赖第三方库

**项目环境说明：**
- Python 3.6.8 （理论3.6及以上肯定可以）
- 第三方依赖库：
- - requests 发送post请求，发送数据
- - psutil 获取操作系统运行相关数据
- - apscheduler 设置定时任务

因为相关依赖较少，你可以直接在本地环境安装使用，也可以创建一个虚拟环境安装使用（Python虚拟环境推荐使用pipenv进行管理，点击我查看pipenv使用教程）。

进入环境后，输入下面pip指令进行安装：
```bash
pip3 install requests psutil apscheduler
```

### 修改钉钉加签密钥和机器人Webhook链接
本地打开`dingding_bot.py`文件，然后修改第20行和第47行代码，换成你自己的钉钉加签密钥和机器人Webhook链接即可。

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3b6d4adb66f4d029ecea978667b3412~tplv-k3u1fbpfcp-zoom-1.image" width=70%/>

### 运行代码
项目文件夹下，直接在终端/CMD中执行下面代码即可，
```bash
python3 scheduler.py
```

### 运行效果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df14aa596f7246308289e9ee8bfc4678~tplv-k3u1fbpfcp-zoom-1.image" width=70%/>


本项目完整教程：[Python+钉钉让你更了解你的云服务器]()

我是老表，和你一起学云服务器开发、Python、Go等。
<img src="https://img-blog.csdnimg.cn/8af3813e46174c57bc7d4a4e0c77f195.png" width=70%/>