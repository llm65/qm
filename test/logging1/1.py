import logging

# 创建日志器对象test，赋值给变量logger
logger = logging.getLogger("test")

# 设置日志最低输出级别
logger.setLevel(logging.DEBUG)

# 添加控制台handler，用于输出日志到控制台
console_handler = logging.StreamHandler()
# 添加日志文件handler，用于输出日志到文件中
file_handler = logging.FileHandler(filename='log.log', encoding='UTF-8')

# 设置格式并赋予handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将handler添加到日志器中
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 输出不同级别日志
logger.debug("============【开始测试】====================")
logger.info("============【开始测试】====================")
logger.warning("============【开始测试】====================")
logger.critical("============【开始测试】====================")
logger.error("============【开始测试】====================")
