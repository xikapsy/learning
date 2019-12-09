import xlwt
#添加工作簿
new_workbook = xlwt.Workbook()
#新建表
worsheet = new_workbook.add_sheet("new_test")
#写入内容
worsheet.write(0,0,"test")
#保存
new_workbook.save(".\\登陆.xlsx")