import openpyxl
from common.all_paths import casexlsx_path


class ExcelMothed:
    def __init__(self, filepath, sheet):
        """
        :param filepath: excel文件路径
        :param sheet: 表名
        """
        self.filepath = filepath
        self.sheet = sheet

    def open_excel(self):
        """获取文件对象"""
        workbook = openpyxl.load_workbook(self.filepath)
        return workbook

    def get_sheet(self):
        """获取Sheet表单"""
        workbook = self.open_excel()
        sheet = workbook[self.sheet]
        return sheet

    def get_case(self):
        """获取所有用例"""
        cell = self.get_sheet()  # 表
        rows = list(cell.rows)  # 总行

        case = []  # 总数据
        title = []  # 首行数据，作为字典的键名

        for row in rows[0]:  # 首行 >> 单元格
            title.append(row.value)  # 存入

        for values in rows[1:]:  # 总行（除首行） >> 单行
            dic = {}  # 创建/重置字典
            for index, value in enumerate(values):  # 单行 >> 索引，单元格
                dic[title[index]] = value.value  # 存入字典，{"列名1"："值", "列名2"："值"...}
            case.append(dic)  # 存入总数据
        return case

    def excel_write(self, row, column, data):
        """excel根据单元格位置写入内容"""
        sheet = self.get_sheet()  # 表
        sheet.cell(row, column).value = data  # 单元格的值 = data
        self.excel_save()  # 保存
        self.excel_close()  # 关闭

    def excel_save(self):
        """保存excel"""
        self.open_excel().save(self.filepath)

    def excel_close(self):
        """关闭excel"""
        self.open_excel().close()


if __name__ == '__main__':
    data1 = ExcelMothed(casexlsx_path, 'Sheet1')
    print(data1.get_case())
