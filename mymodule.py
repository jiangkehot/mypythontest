#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:43:20 2018

@author: jiangke
"""

from math import sqrt

def isPrime_for(n):
    '枚举法素数判断之：for循环'
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
        
# =============================================================================
# def isPrime_while(n):
#     '枚举法素数判断之：while循环'
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         else:
#             return True
#         i += 1
# =============================================================================
    
def isPrime_while(n):
    '枚举法素数判断之：while循环'
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1  
    return True
          
def isPrime(n,isPrime_for = isPrime_for): 
    return isPrime_for(n)
    
def listPrime(n=100):
    '素数列表解析式 '
    print([i for i in range(1,n+1) if isPrime_while(i)])

  
def beishu(n,m=10000):
    '输出m值以内，n的倍数，m默认值为1万'
    sum = n
    while sum <= m:
        print('{:,}'.format(sum),end=' ')
        sum += n