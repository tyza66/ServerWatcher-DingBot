from apscheduler.schedulers.blocking import BlockingScheduler
from data_detection import get_server_info, get_warning, start_info
from dingding_bot import  warning_bot


def start_info_once():
    message = start_info()
    title = '服务器消息'
    # 发消息
    warning_bot(message, title)


'''
1、每天早上9:00 发送服务器情况到钉群
'''
def every_day_nine():
    message = get_server_info()[0]
    title = '服务器基础信息'
    # 发消息
    warning_bot(message, title)


'''
2、时时预警（每30秒检测一次）
'''
def every_seconds_30():
    warning = get_warning()
    if warning != 'ok':
        title = '【⚠️警告】服务器故障'
        warning_bot(warning, title)

start_info_once()

# 选择BlockingScheduler调度器，应用程序可以后台静默运行
sched = BlockingScheduler(timezone='Asia/Shanghai')

# job_every_nine 每天早上9点运行一次  日常发送
sched.add_job(every_day_nine, 'cron', hour=9)

# every_seconds_30 每30s执行一次  数据监控
sched.add_job(every_seconds_30, 'interval', seconds=30)

# 启动定时任务 
sched.start()
