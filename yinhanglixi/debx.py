#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:13:58 2018

@author: jiangke
"""

def debx(a = 200000,m = 36,B = 8.4):
    '求得等额本息每月应还金额x的值'
    b = B / 12 /100
    xa = a * (1 + b) ** m * b
    xb = (1 + b) ** m - 1
    x = xa / xb
#    return ('等额本息每月应还金额为：' + {:} + '元').format(x)
#    return ('等额本息每月应还金额为：' + str(x) + '元')
    return x


def nsybj(n,a = 200000,m = 36,B = 8.4):
    '第n月还款后，剩余本金'
    b = B / 12 /100
    xa = a * (1 + b) ** n
    xb = debx(a,m,B) * ((1 + b) ** n - 1) / b
    sybj = xa - xb
    return sybj

def nlx(n,a,m,B):
    b = B / 12 /100
    return nsybj(n-1,a,m,B) * b

def nbj(n,a,m,B):
    return debx(a,m,B) - nlx(n,a,m,B)

a = int(input('输入贷款金额：'))
m = int(input('输入还款期数：'))
B = float(input('输入年利率：'))
#bs = float(input('输入月服务费：')) / 100
print('等额本息每月应还款金额为：' + str(debx(a,m,B)))

n = int(input('第几个月？'))
print('第' + str(n) + '个月应还本金为：' + str(nbj(n,a,m,B)) +'元!' )
print('第' + str(n) + '个月应还利息为：' + str(nlx(n,a,m,B)) +'元!' )
print('第' + str(n) + '个月还款后剩余本金为：' + str(nsybj(n,a,m,B)) + '元！')

for i in range(1,m+1):
    print('{:18.2f}{:18.2f}{:18.2f}'.format(nbj(i,a,m,B),nlx(i,a,m,B),nsybj(i,a,m,B)))
#    print('第' + str(i) + '个月应还本金为：' + str(nbj(i,a,m,B)) +'元!' )
#    print('第' + str(i) + '个月应还利息为：' + str(nlx(i,a,m,B)) +'元!' )
#    print('第' + str(i) + '个月还款后剩余本金为：' + str(nsybj(i,a,m,B)) + '元！')