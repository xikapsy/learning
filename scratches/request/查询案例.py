import  requests

'''

'''

#登录信息
data1 = {
    "userName" :"zhangquan",
    "password" :"e10adc3949ba59abbe56e057f20f883e"
}
headers = {"Content-Type":"application/json"}
data2 ={
"wowDs": "20191105",
"wowVal": "2",
"wowid": "B0FFFAB6J2"
}
url_login = "http://test-general-field-wow-api.k8s.startdtapi.com/api/v1/recognition/login"
url_daily = "http://test-general-field-wow-api.k8s.startdtapi.com/api/v1/product/daily"


#调用登录

r = requests.post(json = data1,url = url_login)

print(r.json())
login_cookies = r.cookies
print(login_cookies)

r2 = requests.post(url_daily,json = data2,cookies = login_cookies)
print(r2.status_code)
