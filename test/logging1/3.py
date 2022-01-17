import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import time

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
time_rotating_handler1 = TimedRotatingFileHandler('time_rotating_log.log', when='M', interval=2, backupCount=2, encoding='UTF-8', delay=False, utc=False, atTime=time)
# time_rotating_handler1 = TimedRotatingFileHandler('log.log', when="MIDNIGHT", interval=1, backupCount=30)
# TimedRotatingFileHandler：定时创建日志
# 参数：filename-文件路径，when/interval-时间单位/数量，backupCount-最多文件数

"""
when：S秒/M分/H时/D天；W0-6星期1-7/midnight午夜/用这两个时interval无效
interval单位数量
backupCount保留日志文件的个数
翻转时间+发出输出 =创建
"""
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
time_rotating_handler1.setFormatter(formatter)
logger.addHandler(time_rotating_handler1)

# 输出日志记录
logger.debug("============【开始测试】====================")
logger.info("============【开始测试】====================")
logger.warning("============【开始测试】====================")
logger.error("============【开始测试】====================")
logger.critical("============【开始测试】====================")
