import math
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
    sum_x = sum([x[i] for i in range(n)])
    sum_y = sum([y[i] for i in range(n)])
    sum_x_x = sum([ x[i]*x[i] for i in range(n)])
    sum_x_y = sum([x[i]*y[i] for i in range(n)])
    
    if special == True:
        a1 = sum_x_y/sum_x_x
        return a1
    a1 = (n*sum_x_y-sum_x*sum_y)/(n*sum_x_x-sum_x*sum_x)
    a0 = (sum_y*sum_x_x-sum_x*sum_x_y)/(n*sum_x_x-sum_x*sum_x)
    return a0,a1

def non_linear_regression_exponential_form(x,y):
    if len(x) != len(y):
        print("Invalid Argument: incompatible length")
        return

    n = len(x)
    sum_x = sum([x[i] for i in range(n)])
    sum_lny = sum([math.log(y[i]) for i in range(n)])
    sum_x_x = sum([x[i]*x[i] for i in range(n)])
    sum_x_lny = sum([x[i]*math.log(y[i]) for i in range(n)])
    
        
    a1 = (n*sum_x_lny-sum_x*sum_lny)/(n*sum_x_x-sum_x*sum_x)
    a0 = (sum_lny*sum_x_x-sum_x*sum_x_lny)/(n*sum_x_x-sum_x*sum_x)
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

def __main__():
    x = [2.0,3.0,2.0,3.0]
    y = [4.0,6.0,6.0,8.0]
    
    theta = [0.69,0.96,1.13,1.57,1.91]
    T = [0.188,0.209,0.230,0.250,0.313]
    
    eps = [0,0.183,0.36,0.5324,0.702,0.867,1.0244,1.1774,1.329,1.479,1.5,1.56]
    stress = [0,306,612,917,1223,1529,1835,2140,2446,2752,2767,2896]
    
   ## a1 = linear_regression(eps,stress,True)
    t = [0,1,3,5,7,9]
    gamma = [1,0.891,0.708,0.562,0.447,0.355]
    a0,a1 = non_linear_regression_exponential_form(t,gamma)
    x_var = sympy.Symbol('x')
    a_var = sympy.Symbol('a')
    b_var = sympy.Symbol('b')
    
    expr = a_var*sympy.exp(b_var*x_var)
    print(expr.evalf(subs={x_var:24,a_var:a0,b_var:a1}))
    temperature = [80,40,-40,-120,-200,-280,-340]
    coeff_thermal_exp = [6.47e-6,6.24e-6,5.72e-6,5.09e-6,4.30e-6,3.33e-6,2.45e-6]
   ## a = non_linear_polynomial_regression(temperature,coeff_thermal_exp,2)
   ## print(a)
    
__main__()
