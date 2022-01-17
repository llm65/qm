# get_logger()的参数我放到了yaml文件里，所以需要从common里import read_yaml方法、配置文件的路径
import logging
from common.all_paths import config_path, log_path
from common.read_yaml import read_yaml

log_info = read_yaml(config_path)['log']


def get_logger(
        filepath=None,
        fmt=log_info['format'],
        logger_level=log_info['logger_level'],
        stream_level=log_info['stream_level'],
        handler_level=log_info['file_level']
):
    # 创建日志器对象test，赋值给变量logger
    logger = logging.getLogger("test")

    if not logger.handlers:
        # 设置日志最低输出级别
        logger.setLevel(logger_level)

        stream_handler = logging.StreamHandler()  # 添加控制台handler，用于输出日志到控制台
        stream_handler.setLevel(stream_level)  # 控制台handler日志最低输出级别
        logger.addHandler(stream_handler)  # 将handler添加到日志器中

        # 设置格式并赋予handler
        fmt1 = logging.Formatter(fmt)
        stream_handler.setFormatter(fmt1)

        if filepath:
            # 添加文件handler，用于输出日志到文件中
            file_handler = logging.FileHandler(filepath, 'a', encoding='utf-8')
            file_handler.setLevel(handler_level)  # 文件handler日志最低输出级别

            # 设置格式并赋予handler
            file_handler.setFormatter(fmt1)
            logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    get_logger(filepath=log_path).info("用例加载完毕开始执行")
