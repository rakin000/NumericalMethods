import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,30,10000)

def f(x):
    return 2**x-x

def showGraph():
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
    return diff*100/xm_new

def bisectRoot(xl,xu,ep,m_it):
    xm_old = float("NaN") 
    abs_rel_error = [] 
    xm = None
    while xl < xu and  m_it > 0 :
        xm = (xl+xu)/2.0 
        ep_n = error(xm,xm_old)
        abs_rel_error.append([xl,xu,xm,xm_old,ep_n])
        xm_old = xm
        if ep_n <= ep : 
            return xm,abs_rel_error
        if f(xm)*f(xl) < 0.0 : 
            xu = xm
        elif f(xm)*f(xl) > 0.0 :
            xl = xm
        else:
            return xm,abs_rel_error
        m_it -= 1
    return xm,abs_rel_error


def __main__():
    showGraph()

    xL = float(input("Lower Limit: "))
    xH = float(input("Higher Limit: "))
    mit = int(input("Max Iteration: "))
    ep = float(input("Maximum Absolute Relative Error: "))

    x,err = bisectRoot(xL,xH,ep,mit)
    
    print("Iteration\t|\t\tXl\t|\t\tXu\t|\t\tXm\t|\tXm_old\t|\tAbsRelError")
    print("================================================================================================================================")
    for i in range(len(err)):
        print("%4d\t\t|\t%4.7lf\t|\t%4.7lf\t|\t%4.7lf\t|\t%4.7lf\t|\t%4.7lf" %(i,err[i][0],err[i][1],err[i][2],err[i][3],err[i][4]))
    print()
    print("X = ",x)


__main__()

            
