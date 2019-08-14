# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 00:12:54 2019

@author: Disha Bhadauria
"""
from math import sqrt
n=int(input("enter n")) 
for a in range (1,n+1):
    for b in range (1,n):
        c_sq=a**2+b**2
        c=int(sqrt(c_sq))
        if ((c_sq-c**2)==0):
            print(a,b,c)
