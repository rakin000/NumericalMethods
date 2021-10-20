"""
Created on Sat Jul  3 10:58:32 2021

@author: SlaughterHouse
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy 


# gaussian elimination with partial pivoting 
def GaussianElimination(A,B,d=True):
    n = np.size(A,axis=0)
    if n != np.size(A,axis=1):
        print("Invalid Input")
        return 
    if n != np.size(B,axis=0):
        print("Invalid Input")
        return
    
    for i in range(n-1):
        maximum_pivot_element_id = i
        for j in range(i+1,n):
            if abs(A[j][i]) > abs(A[maximum_pivot_element_id][i] ):
                maximum_pivot_element_id = j
        A[[i,maximum_pivot_element_id]] = A[[maximum_pivot_element_id,i]]
        B[[i,maximum_pivot_element_id]] = B[[maximum_pivot_element_id,i]]
        
        for j in range(i+1,n):
            mul = A[j][i]/A[i][i]
            A[j] = A[j] - A[i]*mul
            B[j] = B[j] - B[i]*mul
        if d == True :
            print("After Step %d: "%(i+1))
            print(A)
            print()
            print(B)
            print()
    
    X = np.zeros([n,1])
    
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            B[i] = B[i] - X[j]*A[i][j]
        X[i] = B[i]/A[i][i]
    return X
                

## linear regerssion, y = a0 + a1*x; returns a0 and a1, a1 for special case y=a1*x.
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

def non_linear_regression_exponential_form(x,y):
    if len(x) != len(y):
        print("Invalid Argument: incompatible length")
        return

    n = len(x)
    sum_x = 0
    sum_lny = 0
    sum_x_sq = 0
    sum_x_lny = 0
    
    for i in range(n):
        sum_x += x[i]
        sum_lny += math.log(y[i])
        sum_x_sq += x[i]*x[i]
        sum_x_lny += x[i]*math.log(y[i])
        
    a1 = (n*sum_x_lny-sum_x*sum_lny)/(n*sum_x_sq-sum_x*sum_x)
    a0 = (sum_lny*sum_x_sq-sum_x*sum_x_lny)/(n*sum_x_sq-sum_x*sum_x)
    a0 = math.e ** a0
    return a0,a1


def non_linear_polynomial_regression(x,y,degree):
    if len(x) != len(y) :
        print("Invalid Argument: incompatible length")
        return 
    n = len(x)
    m = degree
    sum_x = [0.0]*(2*m+1)
    sum_y = [0.0]*(2*m+1) 
    
    for p in range(2*m+1):
        for i in range(n):
            tmp = math.pow(x[i],p)
            sum_x[p] += tmp
            sum_y[p] += tmp*y[i]
            
    coeff_matrix = np.zeros((m+1,m+1),dtype=float)
    const_matrix = np.zeros((m+1,1),dtype=float)
    
    for i in range(m+1):
        for j in range(m+1):
            coeff_matrix[i][j] = sum_x[i+j]
        const_matrix[i] = sum_y[i]
   # print(coeff_matrix)
   # print(const_matrix)
    a = GaussianElimination(coeff_matrix, const_matrix, False)
    return a
    
def non_linear_regression_saturation_model(x,y):
    if len(x) != len(y) :
        print("Invalid Argument: incompatible length")
        return
    
    n = len(x)
    _1_x = [1.0/xx for xx in x]
    _1_y = [1.0/yy for yy in y]
    
    a0,a1 = linear_regression(_1_x, _1_y)
    
    a=1.0/a0
    b=a1/a0
    return a,b

def non_linear_power_regression(x,y):
    if len(x) != len(y):
        print("Invalid Argument: incompatible length")
        return 
    n = len(x)
    lnx = [math.log(xx) for xx in x]
    lny = [math.log(yy) for yy in y]
    a0,a1 = linear_regression(lnx,lny)
    a = math.e ** a0
    b = a1
    return a,b



    

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