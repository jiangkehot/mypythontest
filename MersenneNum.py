#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:55:10 2018

@author: jiangke
"""
from mymodule import isPrime

#list =[2 ** P - 1 for P in range(1,5) if isPrime(P)&isPrime(2 ** P -1)]
##print(['{:,}'.format(x) for x in list])
#print(list)

n = 50
print([P for P in range(1,n) if isPrime(P)])
print([2 ** P - 1 for P in range(1,n) if isPrime(2 ** P -1)])


#[3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951]

# =============================================================================
# ['3',
#  '7',
#  '31',
#  '127',
#  '8,191',
#  '131,071',
#  '524,287',
#  '2,147,483,647',
#  '2,305,843,009,213,693,951']
# =============================================================================
