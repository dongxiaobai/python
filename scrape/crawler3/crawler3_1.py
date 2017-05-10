from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,'html.parser')
#未经正则处理
# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])
#经过正则处理
for link in bsObj.find("div",{"id":"bodyContent"})\
.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])