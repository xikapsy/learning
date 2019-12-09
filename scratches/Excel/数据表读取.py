import xlrd

#打开单元表
xlsx = xlrd.open_workbook(".\\登陆.xlsx")
#打开工作表
table = xlsx.sheet_by_index(0)
#获取单元格
print(table.cell_value(1,0))
print(table.cell(0,0).value)
#获取行
print(table.row_values(0))
#获取列
print(table.col_values(0))

