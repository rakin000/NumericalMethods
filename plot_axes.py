import numpy as np
import matplotlib.pyplot as plt 

def plot_axes(plt,x_left,x_right,y_down,y_up):
	x_axis = np.linspace(x_left,x_right,4)
	zeros = np.linspace(0,0,4)
	y_axis = np.linspace(y_down,y_up,4)
	plt.plot(x_axis,zeros)
	plt.plot(zeros,y_axis)
	return plt
