# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:37:28 2021

@author: SlaughterHouse
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy 


def linear_regression(x,y,special=False):
    if len(x) != len(y):
        print("Invalid Argument: incompatible length.")
        return 
    n = len(x)
    sum_x = 0
    sum_y = 0
    sum_x_sq = 0
    sum_x_y = 0;
    
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_x_sq += x[i]*x[i]
        sum_x_y += x[i]*y[i]
    
    if special == True:
        a1 = sum_x_y/sum_x_sq
        return a1
    a1 = (n*sum_x_y-sum_x*sum_y)/(n*sum_x_sq-sum_x*sum_x)
    a0 = (sum_y*sum_x_sq-sum_x*sum_x_y)/(n*sum_x_sq-sum_x*sum_x)
    return a0,a1

def linear_function(a0,a1,x):
    return a0+a1*x

def function(a:np.array,x:np.array):
    res = sum(a[i]*x[i] for i in range(len(a)))
    

data = open("data.txt","r").readlines()
x = []
y = [] 
for line in data:
    inp=line.split()
    x.append(float(inp[0]))
    y.append(float(inp[1]))

a0,a1 = linear_regression(x,y)
y1 = [a0+a1*xx for xx in x]
plot1 = plt
plot1.scatter(x,y)
plot1.plot(x,y1,color='red')
plot1.show()