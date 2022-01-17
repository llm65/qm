import os
dir_name1 = os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.dirname(dir_name1)
log_path = os.path.join(os.path.join(dir_name, 'logs'), 'log.log')  # log文件路径
casexlsx_path = os.path.join(os.path.join(dir_name, 'data'), 'case.xlsx')  # 测试用例excel文件路径
report_path = os.path.join(os.path.join(dir_name, 'reports'), 'report.html1')  # 测试报告文件路径
config_path = os.path.join(os.path.join(dir_name, 'conf'), 'conf.yaml')  # 配置文件路径
case_path = os.path.join(dir_name, 'testcases')  # 测试用例代码路径


if __name__ == '__main__':
    def chinese(data):
        count = 0
        for s in data:
            if ord(s) > 127:
                count += 1
        return "{0:>{wd}}".format(data, wd=24-count)

    print(chinese("公共方法路径："), dir_name1)
    print(chinese("base路径："), dir_name)
    print(chinese("log文件路径："), log_path)
    print(chinese("测试用例excel文件路径："), casexlsx_path)
    print(chinese("测试报告文件路径："), report_path)
    print(chinese("配置文件路径："), config_path)
    print(chinese("测试用例代码路径："), case_path)
