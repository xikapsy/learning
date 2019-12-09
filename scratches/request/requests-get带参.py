import requests # 导入包
"""
    目标：get方法使用-带参
    案例：
        1、http://www.baidu.com?id=101
        2、http://www.baidu.com?id=101,102
        3、http://www.baidu.com?id=101&kw=北京
    请求： get
    参数：
        :params:字典或字符串
    响应：
            1、响应对象.URL  #请求URL
            2、响应对象 .status code #响应状态码
            3、响应对象.text #文本响应内容
"""
url = "http://www.baidu.com"

#1、定义字典
#params = {"id":101}
#2、
#params = {"id":[101,102]} #不推荐
#params = {"id":"101,102"}   # ‘%2C’ 为ASCI为逗号

#3、
params = {"id":"123","wd":"杭州"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

r = requests.get(url,params= params,headers = headers) # r为响应数据对象

#获取请求地址
print("请求url",r.url)
#获取响应码
print("响应code",r.status_code)
#获取响应文本信息
print("响应对象文本",r.content.decode('utf-8'))
#编码方式
print("编码方式",r.encoding)