import requests
"""
Baseapi.py文件封装了接口常用的请求方式
"""


class Baseapi(object):
    def request_get(self, url, query):
        r = requests.get(url=url, query=query)
        return r.json()
     

    def request_post(self):
        pass

    def request_put(self):
        pass

    def request_delete(self):
        pass