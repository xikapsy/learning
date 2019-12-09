import  requests

"""
    目标：post方法使用
    案例：www.baidu.com
    请求： post
    参数：
        1、json : 传入json字符串
        2、headers 传入请求信息头内容
    响应：
            1、响应对象.json()
"""



#请求URL
url: str = "http://test-startdt-offical.startdtapi.com/auth/item/sku/rfid/delete"
#请求headers
headers = {"Content-Type":"application/json"}
#请求json
data = {"skuCode":"20180927170000015412","rfid":"E2806894000040050D43C02C"}

#调用post
r = requests.post(url, json = data,  headers = headers)
print(r.json()) # 返回json
print(r.status_code) #返回状态码