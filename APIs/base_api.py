import logging
import random
import importlib
import copy
import json
import unittest
import dictdiffer


logger = logging.getLogger('main.api')
req_prefix = 'req.'  # 请求、响应
res_prefix = 'res.'


def _separate_data(data, prefix='req.'):  # 将传入字典的key，去掉给定前缀再返回
    pfx = prefix
    result = {}
    for key, value in data.items():
        if key.startswith(pfx):
            req_key = key[len(pfx):]  # 去前缀,如fanyi.req.
            result[req_key] = value
    return result


def _get_cmd(key, dict_name='payload'):  # dict << key，返回一个key= value
    """
    往字典中加key
    :param key: '123'
    :return: payload[123] = value
    多级：
    :param key: '123.ABC'
    :return: payload[123]['ABC'] = value
    """
    separator = '.'  # 分隔符
    cmd = dict_name
    if separator in key:  # key中有'.'
        data_key = key.split(separator)  # 分割
        for each in data_key:  # 遍历
            if each.isdigit():
                # isdigit：检查字符串是不是数字组成
                cmd = cmd + '[' + each + ']'  # 数字不加''
            else:
                cmd = cmd + '[\'' + each + '\']'  # 非数字加''
        cmd = cmd + ' = value'
    else:
        cmd = cmd + f'[{key}] = value'
    return cmd


def check_result(unittest_testcase, x, y):  # 用例，断言
    # 只有x,y完全相同才能通过，任意不同则返回失败。建议自己在用例中做结果检查
    testcase = unittest_testcase
    testcase.assertEqual(x, y)


class BaseAPI(object):
    def __init__(self, api):
        """

        :param api:
        """
        self.api = api

        self.api_name = None
        self.url = ''
        self.req_template = {}  # 模板
        self.res_template = {}

        self._get_api_param()

    def _get_api_param(self):
        """动态加载API定义文件，获取文件中定义的API参数"""
        try:  # 读取，赋值
            m = importlib.import_module(self.api)  # 动态导入别的文件里面的代码
            self.api_name = m.API_NAME
            self.url = m.url
            self.req_template = m.req_param
            self.res_template = m.res_param
        except Exception as e:
            logger.error('error info : %s' % e)

    def payload(self, data=None):
        payload = copy.deepcopy(self.req_template)  # 深层拷贝

        if data:
            req_pre = '.'.join([self.api_name, req_prefix])
            # req_prefix：请求前缀
            # .join：拼接
            # req_pre：self.api_name.req_prefix
            req_data = _separate_data(data, req_pre)  # 调用'去前缀函数'

            for key, value in req_data.items():  # 读取数据，更新数据
                cmd = _get_cmd(key, 'payload')  # 调用加key函数
                exec(cmd)
        return payload


    def load_expected(self, data=None):
        expected = {'success': True}
        if data:
            # res_pre = '.'.join([self.api_name, res_prefix])
            # res_data = _separate_data(data, res_pre)
            for key, value in data.items():
                cmd = _get_cmd(key, 'expected')
                exec(cmd)
        return expected


# llm = BaseAPI('Testcase.API.Case.baidu')
# print(llm.api_name)
# print(llm.req_template)
# print(llm.res_template)
# print(llm.url)
