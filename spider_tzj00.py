#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 11:20:26 2018

@author: jiangke
"""

import requests
from bs4 import BeautifulSoup
import random
import time

def childname(tags):
    '返回所有子节点的名称'
    return print([tag.name for tag in tags.children])

def zsname(tags):
    '返回所有子孙节点的名称'
    return print([tag.name for tag in tags.descendants])

#def spider(url):
#    r = requests.get(url)
#    soup = BeautifulSoup(r.text,'lxml')
##    code = soup.find('div','main box-zdb')
##    soup_new = BeautifulSoup(str(code),'lxml')
##    return soup
for i in range(1,2):
    url = 'http://zdb.pedaily.cn/inv/p' + str(i) + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    news = soup.find('div','list-time list-zdb list-invest')
#    with open('tzjnews.html','w') as f:
#        f.write(str(news.prettify()))
        
# =============================================================================
#     li = news.ul.contents
#     for i in range(1,21):
#         date = li[i].div.get_text
#         dl = li[i].dl.contents
#         print('~~~~~~~~~~~~')
#         for x in range(5):
#             print(dl[x]['class'],':',dl[x].string)
# =============================================================================

    for li in news.ul.children:
        print('~~~~~~~~~~~~~~~~~')
        if li.attrs == {}:
            updatetime = li.div.span.contents
            print('更新日期：{}'.format(updatetime[1]))           
            for dt in li.dl.children:
                if dt['class'] == ["money"]:
                    print(dt['class'],':',end='')
                    for dtspan in dt.children:
                        print(dtspan.string,end='/')
                    print()
                elif dt['class'] == ["group"]:
                    print(dt['class'],':',end='')
                    for dta in dt.children:
                        print(dta.string,end='')
                    print()
                else:
                    print(dt['class'],':',dt.string)
    
    s = random.randint(1,10)
    time.sleep(s)
        
    
