# 云你好 python sdk
import requests


class HelloSDK:
    # 云你好服务地址
    service_url = "http://127.0.0.1:5000/api/hello"

    @classmethod
    def hello(cls, name):
        response = requests.get(url=cls.service_url, params={"name": name})
        return response.text

# 欢迎使用云你好 python sdk，您可以通过以下方式使用 sdk：
# 安装云你好 sdk：pip install hello-sdk
# 使用你好云 sdk：
# from hello_sdk import HelloSDK

# HelloSDK.hello("阿菌")