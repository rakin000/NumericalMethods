import numpy as np
import matplotlib.pyplot as plt 

def plot_axes(plt,x_left,x_right,y_down,y_up):
	x_axis = np.linspace(x_left,x_right,4)
	zeros = np.linspace(0,0,4)
	y_axis = np.linspace(y_down,y_up,4)
	plt.plot(x_axis,zeros)
	plt.plot(zeros,y_axis)
	return plt

vds1 = [0,1,2,3,4,5,6,7,8,9,10]
id1 = [0,0,0,0,0,0,0,0,0,0,0]
vds2 = [0,0.0042,0.00211,0.444,0.950,1.56,2.38,3.36,4.34,6.31,7.30,8.28,10.3]
id2 = [0,0.058,0.289,5.56,10.5,14.4,16.2,16.4,16.6,16.9,17.0,17.2,17.5]
vds3 = [0,0.00279,0.028,0.0561,0.113,0.227,0.286,0.585,0.901,1.24,1.59,1.98,2.9,3.47,6.11,8.96,13.7]
id3 = [0,0.0721,0.72,1.44,2.87,5.73,7.14,14.1,21,27.6,34.1,40.2,51,55.3,58.9,60.4,63.1]

def showGraph():
    plt.plot(vds1,id1,label='At VGS = 0 V')
    plt.plot(vds2,id2,label='At VGS = 3 V')
    plt.plot(vds3,id3,label='At VGS = 5 V')
    plt.grid(True)
    plt.title("MOSFET Characteristics")
    plt.legend()
    plt.ylabel("ID (mA) ")
    plt.xlabel("VDS (V) ")
    plt.show()    
plot_axes(plt,-3,15,-20,80)
showGraph()