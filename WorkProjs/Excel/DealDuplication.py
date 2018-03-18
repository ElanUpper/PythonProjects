# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DealDuplication
   Description :
   Author :       elan
   date：          3/9/2018
-------------------------------------------------
   Change Activity:
                   3/9/2018:
-------------------------------------------------
"""

import xlrd
from datetime import date, datetime
from collections import Counter


def read_excel():

	# excel_name = r'C:\Users\elan\Desktop\test.xlsx'
	excel_name = r'C:\Users\elan\Desktop\SR_Raw_Problem_Description.xlsx' ;

	# 文件位置
	ExcelFile = xlrd.open_workbook(excel_name)

	# 获取目标EXCEL文件sheet名
	print(ExcelFile.sheet_names())

	# ------------------------------------
	# 若有多个sheet，则需要指定读取目标sheet例如读取sheet2
	# sheet2_name=ExcelFile.sheet_names()[1]
	# ------------------------------------

	# 获取sheet内容【1.根据sheet索引2.根据sheet名称】
	# sheet=ExcelFile.sheet_by_index(1)
	sheet = ExcelFile.sheet_by_name('SR_Raw_Problem Description')
	# 打印sheet的名称，行数，列数
	print(sheet.name, sheet.nrows, sheet.ncols)

	# 获取整行或者整列的值
	#rows = sheet.row_values(2)  # 第三行内容 0开始计数
	cols = sheet.col_values(2)
	ret_counter  = dict(Counter(cols))
	dump_counter = {k:v for k, v in ret_counter.items() if v > 1 }
	print(list(dump_counter.keys()))  # 仅仅打印出key

	# 获取单元格内容
	#print(sheet.cell(1, 0).value.encode('utf-8'))
	#print(sheet.cell_value(1, 0).encode('utf-8'))
	#print(sheet.row(1)[0].value.encode('utf-8'))

	# 打印单元格内容格式
	#print(sheet.cell(1, 0).ctype)

if __name__ == '__main__':
	read_excel()

