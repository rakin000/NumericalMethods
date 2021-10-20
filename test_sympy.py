# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:56:00 2021

@author: SlaughterHouse
"""
"""

x = Symbol('x')
f = (x-3)*(x+34)
f_prime = integrate(f)
f2 = differentiate(f)
print(f)
print(f2)
print(f_prime)
f_prime = lambdify(x,f_prime)
print( f_prime(1))
"""
import sympy
x, y = sympy.symbols("x y")
expr = x*y

F = sympy.Function("x*y")

print(F(x = 34,y = 3))
print(expr)