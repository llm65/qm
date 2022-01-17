import pandas as pd
# import openpyxl
file = '../data/user_login.xls'  # excel文件位置


def read_excel():
    """
    调用后读取data.xlsx的数据，并以列表套字典的格式返回
    """
    file_data = pd.read_excel(file, dtype={"列名": "object"}, keep_default_na=False)
    # dtype = {"列名": "object"}：字符串内容为数字时默认会识别成int，加上这个让指定列的数据不换类型
    # keep_default_na = False：空值不为nan

    data_dict = file_data.to_dict('records')
    return data_dict


def result(index, value):
    """
    传入用例索引、执行结果
    在excel中那条用例的result列写入执行结果

    示例：
    result(3, '测试通过')  # 第三条用例，实际结果为测试通过
    """
    v = read_excel()
    v[index-1]['result'] = value
    pd.DataFrame(v).to_excel(file, index=False)


if __name__ == '__main__':
    print(read_excel())
