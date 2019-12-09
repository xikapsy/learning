#导入webdriver 模块 和Excel包
import xlwt
from selenium import webdriver

#实例一个webdriver 对象
driver = webdriver.Chrome("C:\\chromedriver.exe")
#设置隐形等待时间,仅适用于find方法
driver.implicitly_wait(10)
#打开51job。com
driver.get('http://www.51job.com')
# 找到 元素（element） id="kwdselectid"的组件
ele_kwdselect = driver.find_element_by_id("kwdselectid")
#输入"python"
ele_kwdselect.send_keys("python")

# 找到 元素（element） id="work_position_input"的组件
ele_work_position = driver.find_element_by_id("work_position_input")
#点击
ele_work_position.click()


#选择多个元素用find_elements_by_css_selector
#选择单个元素用find_element_by_css_selector
ele_citys = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000   em[class=on]")

for ele in ele_citys:
    ele.click()

#选择的单个城市
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#保存城市选择
driver.find_element_by_id("work_position_click_bottom_save").click()

#点击搜索
driver.find_element_by_css_selector(".ush button").click()
#查找工作内容
jobs = driver.find_elements_by_css_selector("#resultList div[class=el]")

book = xlwt.Workbook()

sh = book.add_sheet("统计")
#输出
row = 0
for job in jobs:
    fields = job.find_elements_by_tag_name("span")
    col = 0
    for field in fields:
        text = field.text
        print(text,end='')
        sh.write(row,col,text)
        col += 1

    print("")
    row += 1
#保存到...
book.save("D:\\51job.xls")

#退出代理
driver.quit()


