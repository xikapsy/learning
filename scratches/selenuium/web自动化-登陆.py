#导包
import unittest
from HTMLTestRunner  import HTMLTestRunner
import time
import xlwt
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#打开webdriver
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
#获取表格对象
wb_data = xlrd.open_workbook(".\\登陆.xlsx")
sheet_data = wb_data.sheet_by_name("数据")
wb_result =copy(wb_data)
sheet_result = wb_result.get_sheet(0)



#定义测试类
class TestCase1(unittest.TestCase):

    #测试环境搭建
    def setUp(self):

        driver.get('http://wgy.pub/#/login')
    #测试环境关闭
    def tearDown(self):

        driver.quit()


    # 测试用例
    def test_Case1(self):
        n = 0
        for username in sheet_data.col_values(0):
            passwd = sheet_data.col_values(1)[n]
            n += 1
            #查找元素
            ele_username =driver.find_element_by_name("username")
            ele_passwd = driver.find_element_by_name("password")
            #输入
            ele_username.send_keys(username)
            ele_passwd.send_keys(passwd)
            # 点击登陆
            ele_login_button = driver.find_element_by_class_name(
                "el-button.el-button--primary.el-button--medium")
            ele_login_button.click()
            time.sleep(1)
            #获取提示
            ele_content = driver.find_element_by_class_name("el-message__content")

            if ele_content.text == "登录成功":
                sheet_result.write(0, 2, ele_content.text)
                wb_result.save(".\\登陆.xlsx")
                time.sleep(3)
                ele_dropdown_selfdefine = driver.find_element_by_class_name(
                    "avatar-wrapper.el-dropdown-selfdefine        ")
                ele_dropdown_selfdefine.click()
                time.sleep(0.5)
                ele_divided = driver.find_element_by_class_name(
                    "el-dropdown-menu__item.el-dropdown-menu__item--divided")
                ele_divided.click()

            elif ele_content.text == "当前用户还未注册，或已经删除":
                sheet_result.write(n - 1, 2, ele_content.text)
                wb_result.save(".\\登陆.xlsx")
                #清空异常数据
                ele_username.send_keys(Keys.CONTROL, 'a')
                ele_username.send_keys(Keys.BACK_SPACE)
                ele_passwd.send_keys(Keys.CONTROL, 'a')
                ele_passwd.send_keys(Keys.BACK_SPACE)
                time.sleep(7)

            elif ele_content.text == "当前用户登录名或密码错误":
                sheet_result.write(n - 1, 2, ele_content.text)
                wb_result.save(".\\登陆.xlsx")
                ele_username.send_keys(Keys.CONTROL, 'a')
                ele_username.send_keys(Keys.BACK_SPACE)
                ele_passwd.send_keys(Keys.CONTROL, 'a')
                ele_passwd.send_keys(Keys.BACK_SPACE)
                time.sleep(7)

            else:
                sheet_result.write(n - 1, 2, "未知错误")
                wb_result.save(".\\登陆.xlsx")
                ele_username.send_keys(Keys.CONTROL, 'a')
                ele_username.send_keys(Keys.BACK_SPACE)
                ele_passwd.send_keys(Keys.CONTROL, 'a')
                ele_passwd.send_keys(Keys.BACK_SPACE)
                time.sleep(7)
            if n>4:
                break




if __name__ == '__main__':
    # 测试用例集合
    suite = unittest.TestSuite()
    # 添加测试用例
    suite.addTest(TestCase1('test_Case1'))

    dir_path = './'
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = dir_path + now + ' HTMLTestRunner.html'
    # 打开文件，写入测试结果
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='Math测试报告', description='用例执行详细信息')
        runner.run(suite)
    f.close()
