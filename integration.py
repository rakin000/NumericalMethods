import math

def abs_rel_error(new_val,old_val):
    return abs((new_val-old_val)/new_val)*100.0

u = 2000.0
q = 2100.0
g = 9.8
m0 = 140000.0
def f(t):
    return u*math.log(m0/(m0-q*t))-g*t

def F(t):
    return u*t*math.log(m0/(m0-q*t))+u*t+(m0/q)*u*math.log(m0-q*t)-(0.5)*g*t*t

def integrate_trapezoid_rule(a,b,n):
    h = (b-a)/n
    summation_f = f(a)+f(b)
    for i in range(1,int(n)):
        summation_f += 2.0*f(a+i*h)

    res = summation_f*h*(1.0/2.0)
    return res 

def integrate_simpson_method(a,b,n):
    h = (b-a)/n
    summation_f = f(a)+f(b)
    for i in range(1,int(n),2):
        summation_f+= 4.0*f(a+i*h)
		
    for i in range(2,int(n-1),2):
        summation_f+=2.0*f(a+i*h)
		
    res = summation_f*h*(1.0/3.0)
    return res

def show_result_trapezoid_rule(a,b,n):
    exact_value = F(b)-F(a)
    prev_approx = float("nan")
     
    print("\tn\t\tApprox Value\t\tTrue Error\t\tAbsRelTrueError\t\tAbsRelError")
    print("------------------------------------------------------------------------------------------------------")
    for n_ in range(1,int(n)+1):
        approx = integrate_trapezoid_rule(a,b,n_)
        true_error = exact_value-approx
        abs_rel_true_e = abs_rel_error(exact_value,approx)
        abs_rel_e = abs_rel_error(approx,prev_approx)
        prev_approx = approx
        print("\t%d\t\t%lf\t\t%lf\t\t%lf\t\t%lf"%(n_,approx,true_error,abs_rel_true_e,abs_rel_e))
    print()

def show_result_simpson_method(a,b,n):
    exact_value = F(b)-F(a)
    prev_approx = float("nan")
    
    print("\tn\t\tApprox Value\t\tTrue Error\t\tAbsRelTrueError\t\tAbsRelError")
    print("------------------------------------------------------------------------------------------------------")
    for n_ in range(1,int(n)+1):
        approx = integrate_simpson_method(a,b,2*n_)
        true_error = exact_value-approx 
        abs_rel_true_e = abs_rel_error(exact_value,approx)
        abs_rel_e = abs_rel_error(approx,prev_approx)
        prev_approx = approx
        print("\t%d\t\t%lf\t\t%lf\t\t%lf\t\t%lf"%(2*n_,approx,true_error,abs_rel_true_e,abs_rel_e))
    print()

def __main__():
    a = float(input("a ?= "))
    b = float(input("b ?= "))
    n = float(input("Number of segments = "))

    trapezoid = integrate_trapezoid_rule(a,b,n)
    simpson = integrate_simpson_method(a,b,2*n)
    print("Using trapezoid rule = %.5lf"%trapezoid)
    print("Using simpson's method = %.5lf"%simpson)
    print()

    
    print("Trapezoid Rule")
    show_result_trapezoid_rule(a,b,n)
    print()

    print("Simpson's Method")
    show_result_simpson_method(a,b,n)
    print()
__main__()

