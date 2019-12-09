import  requests

'''
    1、cookies：获取响应cookies信息
    2、content:以字节码形式获取响应信息
'''

#登录信息
data = {
    "loginKey" :'startdtoperation@startdt.com',
    "merchantId" : "0",
    "password" :"377ea8b8947b5da92ff90e9f3edafb33",
    "redirectUrl" :"http://test-console-admin.startdt.net",
    "useragent" :"h5"
}
url_login = "http://test-sso.startdtapi.com/user/login"
#调用登录

r = requests.post(url= url_login,json = data)

#获取响应cookies
print(r.cookies)
#获取cookies值
print(r.cookies["SERVERID"])
#同上
print(r.cookies.get_dict())

lgoin_cookies = {"SERVERID":r.cookies["SERVERID"] }
