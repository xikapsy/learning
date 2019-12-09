#encoding:utf-8
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib import request
from urllib import parse
from http.cookiejar import MozillaCookieJar


#cookie
cooliejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cooliejar)
opener = request.build_opener(handler)
#url
url = "http://www.baidu.com"
resp = opener.open(url)
print(resp.getcode())
#urlretrieve 下载文件（URL，name）
# request.urlretrieve(url,"baidu.html")
#保存cookie,ignore_discard即将过期的cookie
cooliejar.save(ignore_discard=True)

#urlencode 可以进行编译
#name=%E5%BC%A0%E4%B8%89&greet=hello+word
params= {"name":"张三",'greet':'hello word'}
result = urlencode(params)
print(result)
#parse.parse_qs 反编译
qs = parse.parse_qs(result)
print(qs)
url1 = url+"?"+result
resp1= urlopen(url1)
print(resp1.read())

