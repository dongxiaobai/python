import re
import pandas as pd
import requests

response = requests.get("https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4962&productId=5089225&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1")
response = response.text

pat = '"content":"(.*?)","'
res = re.findall(pat, response)

for i in res:
    i = i.replace("\\n", '')
    print(i)


