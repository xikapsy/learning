import requests
from  pprint import pprint

resBaidu =requests.get('https://www.baidu.com')
print(resBaidu.status_code)
