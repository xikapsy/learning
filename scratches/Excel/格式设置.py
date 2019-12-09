import xlrd
import xlwt
from xlutils.copy import copy
#formatting_info 模板设为打开
tem_excel = xlrd.open_workbook(".\\登陆.xlsx",formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)
#设置格式
style = xlwt.XFStyle()
#字体格式设置
font =xlwt.Font()
font.name = "微软雅黑"
#加粗
font.bold = True
font.height = 100
style.font = font
#边框设置
borders = xlwt.Borders()
#单面  THIN 细线
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

#对齐
aligment = xlwt.Alignment()
aligment.horz = xlwt.Alignment.HORZ_CENTER
aligment.vert = xlwt.Alignment.VERT_BOTTOM
style.alignment = aligment


new_sheet.write(0,0,style)
