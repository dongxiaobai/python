import re
import pandas as pd
import requests
import json

f=open('comment_iphone8_3.txt', 'a')
for i in range(0,200):#20
    try:
        response = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4962&productId=5089225&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
        response = response.text
        #正则方法：简单快捷；缺点：会有重复的
        #pat = '"content":"(.*?)","'
        #res = re.findall(pat,response)
        #for i in res:
            #i = i.replace('\\n', '')
            #print(i)
            #f.write(i)
            #f.write('\n')
        #数组处理方法：可以去掉重复的选项


        response = response[26:-2]#将获取到的内容去掉开头和结尾
        response = json.loads(response)#将字符串转为json对象 dict
        responseComments = response['comments']# list
        
        #print(type(response))#dict 
        for i in responseComments:
            f.write(i['content'])
            f.write('\n')

        #for key, value in responseComments.items():
            #if key == 'content':
                #print(str(value['content']))
                #f.write(str(value))
                #f.write('\n')
                #print(key, ' value: ', value)
                #print(value)
        
    except:
        print('爬取第'+str(i)+'页出现问题')
        continue
f.close()
