import xlrd
import xlwt
from xlutils.copy import copy

#读取工作簿
wb_data = xlrd.open_workbook(".\\登陆.xlsx")
#获取工作表
sheet_data = wb_data.sheet_by_name("数据")
#复制工作簿
wb_result =copy(wb_data)
#获取新工作表
sheet_result = wb_result.get_sheet(0)

print(sheet_result)
#获取行内容
print(sheet_data.row_values(1)[0])
#获取列内容
print(sheet_data.col_values(1))
n =0
for username in sheet_data.col_values(0):
    print(username)
    passwd = sheet_data.col_values(1)[n]
    print(passwd)
    n += 1
    sheet_result.write(n-1, 2, "pass")
    wb_result.save(".\\登陆.xlsx")