#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:15:35 2018

@author: jiangke
"""

from math import sqrt


def isPrime(n):
    '枚举法素数判断之：for循环'
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def mersenneNum(n=5):
    l = [2 ** P - 1 for P in range(1,n ** 2) if isPrime(P)&isPrime(2 ** P -1)]
    return l[n]

print(mersenneNum(6 - 1))
    