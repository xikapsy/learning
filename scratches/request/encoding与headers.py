"""
    目标：响应对象常用方法
        1、encoding
            1）获取请求编码
            2）设置响应编码
        2、headers
            1）获取响应信息头信息
    案例： http://www.baidu.com

"""

import requests

url = "http://www.baidu.com"

r = requests.get(url)

#查看默认请求编码 ISO-8859-1
print(r.encoding)

#设置响应编码
r.encoding = "utf-8"

#查看响应信息
print(r.text)

#查看响应信息头
#项目工作汇总一般服务器返回的token\session相关信息都在headers中
print(r.headers)