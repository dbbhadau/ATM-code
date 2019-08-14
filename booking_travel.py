# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:59:14 2019

@author: Disha Bhadauria
"""

travel=input("yes or no ")
while travel == 'yes':
    num=int(input("tot people travel "))
    for num in range(1,num+1):
        age=input("enter age  ")
        sex=input("enter sex  ")
        name=input("enter name  ")
        print(name)
        print(age)
        print(sex)
    travel=input("forgot someone??  ") 