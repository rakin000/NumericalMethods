import matplotlib.pyplot as plt
import numpy as np

r = 3.0
V = 4.0

def f(x):
    return r*x*x*(3.0*r-x)-3.0*V

def plot_graph(x_left,x_right):
    divisions = 100000
    x = np.linspace(x_left,x_right,divisions)
    y = np.linspace(f(x_left),f(x_right),divisions)
    zeros = np.linspace(0,0,divisions)
    plt.plot(x,zeros)
    plt.plot(zeros,y)
    plt.plot(x,f(x),label='f(x)')
    plt.grid(True)
    plt.title("f(x)")
    plt.legend()
    plt.show()

def error(xm_new,xm_old):
    diff = xm_new-xm_old
    if diff < 0.0 :
        diff = -diff
    if xm_new == 0.0:
        diff+=0.00000001
        xm_new += 0.00000001
    return diff*100.0/abs(xm_new)

def find_root_bisection(xl,xu,ep,m_iteration):
    xm_old = float("NaN") 
    xm = None
    while xl < xu and  m_iteration > 0 :
        xm = (xl+xu)/2.0 
        ep_n = error(xm,xm_old)
        xm_old = xm
        if ep_n <= ep : 
            return xm
        if f(xm)*f(xl) < 0.0 : 
            xu = xm
        elif f(xm)*f(xl) > 0.0 :
            xl = xm
        else:
            return xm
        m_iteration -= 1
    return xm


def __main__():
    plot_graph(0,6)

    xL = float(input("Lower Limit: "))
    xH = float(input("Higher Limit: "))
    max_iteration = int(input("Max Iteration: "))
    ep = float(input("Maximum Absolute Relative Error: "))

    x = find_root_bisection(xL,xH,ep,max_iteration)
    
    print("X = ",x)
    print(f(x))


__main__()
