import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6]
m1 = [0.0205,0.01108,0.02059,0.2708,3.4365,50.5702]
q1 = [0.0161,0.01023,0.1923,18.3373,1840.7850,261823.9506]
m2 = [0.0150,0.0035,0.0210,0.2796,3.4236,42.3814]
q2 = [0.0129,0.0479,0.3699,36.0456,3586.4785,380210.8088]
m3 = [0.0199,0.0022,0.0212,0.2825,3.4235,38.8009]
q3 = [0.0108,0.0040,0.0415,0.5473,6.4872,76.2583]


def showGraph():
    plt.plot(x,m1,label='Merge Sort - Ascending Order')
    plt.plot(x,m2,label='Merge Sort - Descending Order')
    plt.plot(x,m3,label='Merge Sort - Random Order')
    plt.plot(x,q1,label='Quick Sort - Ascending Order')
    plt.plot(x,q2,label='Quick Sort - Descending Order')
    plt.plot(x,q3,label='Quick Sort - Random Order')
    plt.grid(True)
    plt.title("Average Time for Sorting n Integers in Different Input Orders.")
    plt.legend()
    plt.ylabel("Time (milliseconds)")
    plt.xlabel("Input Size (10^n)")
    plt.show()    

def __main__():
    showGraph()

__main__()

            
