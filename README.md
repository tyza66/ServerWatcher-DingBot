- [使用方法](#使用方法)
  - [下载项目文件](#下载项目文件)
  - [安装项目依赖第三方库](#安装项目依赖第三方库)
  - [修改钉钉加签密钥和机器人Webhook链接](#修改钉钉加签密钥和机器人webhook链接)
  - [运行代码](#运行代码)
  - [运行效果](#运行效果)
  - [创建守护进程](#创建守护进程)


<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d802d52dfd147768c1cf687009afd02~tplv-k3u1fbpfcp-zoom-1.image" width=70%/>

## 使用方法
本项目创建了一个钉钉群机器人，设置两种响应<br>
1、每天早上9:00 发送服务器情况到钉群（包括CPU 负载 存储等数据）<br>
2、时时预警，每30s检测一次（监控负载 CPU使用率情况，超过阀值，钉钉消息报警）

### 下载项目文件
```bash
# ssh下载
git clone git@github.com:tyza66/ServerWatcher-DingBot.git
# https下载
git clone https://github.com/tyza66/ServerWatcher-DingBot.git
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

### 创建守护进程
经过上面我们完成了功能复现，但是会发现，一旦我们关闭程序，提醒监测服务也会停止，所以我们需要创建一个守护进程来保护我们的进程。

以我自己为例，我们登录宝塔面板后，进入`/etc/systemd/system`文件夹下，新建一个`ding_bot.service`文件，并写入下面内容：
```bash
[Unit]
Description=Dingding Bot service

[Service]
Type=forking
ExecStart=/bin/bash -c "/usr/bin/python3 /home/software/ServerWatcher-DingBot/scheduler.py &"
KillMode=process
Restart=on-failure
RestartSec=3s

[Install]
WantedBy=multi-user.target
```

简单解释下`Service`里设置的含义，`Type=forking`表示程序启动后，会放到后台运行；`ExecStart`服务的具体执行指令（执行scheduler.py文件即可）；`KillMode=process`表示服务停止的同时也会杀死程序主进程；`Restart=on-failure`表示系统发生意外导致程序退出时，程序自动重启。

保存好文件后，我们直接终端内执行下面指令即可开启进程守护，运行后会进入守护进程状态，我们可以按ctrl+c退出，不会影响守护进程：
```bash
systemctl start ding_bot
```

代码修改后，需要重启守护进程，修改代码才会生效，重启指令如下：
```bash
systemctl restart ding_bot
```

如果不想设置这个守护进程了，执行stop指令可以停止该service（程序也会停止），指令如下：
```bash
systemctl stop ding_bot
```

### 新维护版本
- https://github.com/MutantCat-Working-Group/Echoes

Fork From：[老表](https://python-brief.com)（XksA-me）  
Change By：tyza66



