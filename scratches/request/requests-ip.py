#encoding:utf-8

import  requests
#代理IP
proxy = {
    "http":"113.65.251.197:8118"
}

response = requests.get("http://httpbin.org/ip",proxies = proxy)

print(response.text)
