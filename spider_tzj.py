#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:40:07 2018

@author: jiangke
"""

import requests
from bs4 import BeautifulSoup
import random
import time

tstart = time.time()

for i in range(501,601):
    url = 'http://zdb.pedaily.cn/inv/p' + str(i) + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    news = soup.find('div','list-time list-zdb list-invest')
#    strnews = str(news.prettify())
    j = (i-1) // 100
    filename = 'filename'+ '{:>02}'.format(j) + '.html'

    with open(filename,'a+') as f:
        f.write(str(news))
        
#    with open('data.text','a+') as f:
#        for li in news.ul.children:
#            f.write('~~~~~~~~~~~~~~~~~~~~')
#            if li.attrs == {}:
#                updatetime = li.div.span.contents
#                f.write('更新日期：{}'.format(updatetime[1]))           
#                for dt in li.dl.children:
#                    if dt['class'] == ["money"]:
#                        f.write(str(dt['class'] + ':'))
#                        for dtspan in dt.children:
#                            f.write(dtspan.string,end='/')
#                        f.write()
#                    elif dt['class'] == ["group"]:
#                        f.write(dt['class'],':',end='')
#                        for dta in dt.children:
#                            f.write(dta.string,end='')
#                        f.write()
#                    else:
#                        strdown = str(dt['class']) + ':' + dt.string
#                        f.write(strdown)
        
        s = random.randint(1,2)
        time.sleep(s)
        timenow = time.time()
        tt = (timenow - tstart) / 60
        print('第{0:2d}次更新，{1:2d}s后再次更新，总计用时{2:>5.2f}min'.format(i,s,tt))
                
def newsprettify(filename):
    soup = BeautifulSoup(open(filename,'r'),'lxml')
    news = soup.prettify()
    strnews = str(news)
    with open(filename,'w') as f:
        f.write(strnews)
        
newsprettify(filename)