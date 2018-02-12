# -*- coding: utf-8 -*-

# py3

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib import request
import re

driver = webdriver.Chrome()

first_url = "https://www.zhihu.com/question/XXXXXXX" #问题的回答的网址

driver.get(first_url)

for i in range(30):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 滑动到浏览器底部
    time.sleep(2) 
    try:
        driver.find_element_by_css_selector('button.QuestionMainAction').click() # 选中并点击页面底部的加载更多
        print("page" + str(i)) 
        time.sleep(1) 
    except:
        break

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

req = request.Request(url = first_url,headers = headers)

response = request.urlopen(req)

html = response.read()

soup = BeautifulSoup(html,'html.parser',from_encoding = 'gbk')

imgs = soup.find_all('img',src = re.compile(r'https://pic\d\.zhimg.com/v2-\w+\.jpg'))#这个根据url的不同要改变

i = 1


for img in imgs:
    url = img['src']
    
    req = request.Request(url = url,headers = headers)
    
    data = request.urlopen(req).read()
    
    with open('%s.jpg'%i,'wb') as f:
        
        f.write(data)
        
        
    i += 1
         
