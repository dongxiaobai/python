from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'html.parser')

#处理子标签和其他后代标签
#for child in bsObj.find("table",{"id":"giftList"}).children:
#	print(child)
#处理兄弟标签
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
# 	print(sibling)
#处理父标签
#print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())