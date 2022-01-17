import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
rotating_handler = logging.handlers.RotatingFileHandler('rotating_log.log', encoding='UTF-8', maxBytes=1024, backupCount=5)
"""
maxBytes：日志文件大小，单位为字节
backupCount：备份文件数量
"""
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)

# 输出日志记录
for i in range(150):
    logger.debug(f"{i}")
