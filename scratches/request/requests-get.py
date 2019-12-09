import requests # 导入包
"""
    目标：get方法使用
    案例：www.baidu.com
    请求： get
    响应：
            1、响应对象.URL  #请求URL
            2、响应对象 .status code #响应状态码
            3、响应对象.text #文本响应内容
"""

r = requests.get("http://www.baidu.com") # r为响应数据对象
#获取请求地址
print("请求url",r.url)
#获取响应码
print("响应code",r.status_code)
#获取响应文本信息，猜测编码方式
print("响应对象文本",r.text.encode('utf-8'))
#获取响应文本信息,指定utf-8编译
print("响应对象文本",r.content.decode('utf-8'))
#编码方式
print("编码方式",r.encoding)