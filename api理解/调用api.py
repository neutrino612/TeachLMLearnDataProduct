# 我是云你好服务的一名客户，我通过发送 http get 请求使用云你好

import requests

# API 地址
url = "http://127.0.0.1:5000"
# 发送 GET 请求
response = requests.get(url=url, params={"name": "阿菌"})
# 打印响应结果
print(response.text)