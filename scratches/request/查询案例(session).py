import  requests

'''

'''

#登录信息
data1 = {
    "userName" :"zhangquan",
    "password" :"e10adc3949ba59abbe56e057f20f883e"
}

data2 ={
"wowDs": "20191105",
"wowVal": "2",
"wowid": "B0FFFAB6J2"
}
url_login = "http://test-general-field-wow-api.k8s.startdtapi.com/api/v1/recognition/login"
url_daily = "http://test-general-field-wow-api.k8s.startdtapi.com/api/v1/product/daily"

#获取session对象
session = requests.session()

#调用登录
r =session.post(json = data1,url = url_login)

print(r.json())
#调用查询数据接口
r2 = session.post(url_daily,json = data2)
print(r2.status_code)
