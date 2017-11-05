import requests #导入模块
r = requests.get("http://pythontab.com/justTest") #无参数的get请求

payload = {'key1':'value1','key2':'value2'}
r1 = requests.get("http://pythontab.com/justTest", params = payload)

r2 = requests.post("http://pythontab.com/justTest", data = {"key":"value"})
