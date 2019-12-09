#导包
import unittest
from HTMLTestRunner  import HTMLTestRunner
import time
import xlwt
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#实例一个webdriver 对象
driver = webdriver.Chrome("C:\\chromedriver.exe")
#打开51job。com
driver.get('https://www.zhipin.com/')
# 找到 元素（element） id="kwdselectid"的组件
r= driver.find_element_by_xpath('//div[contains(@class,"home-sider")] |//dd[@class="icon-arrow-right"]')

print(r.text)

driver.close()