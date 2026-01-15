import numpy as np
from scipy.interpolate import interp1d
import types
import scipy
from matplotlib.pyplot import *

def varconvolve(x,y,kernel,var,oversample=1,mode='same'):

	"""
	x: an array with x coordinates of the points
	y: ana rray with y coordinates of the points
	kernel: name of the function that describes the kernel. Must have one argument, the width of the kernel in x units
	var: a function that returns the kernel width in one point.
	"""

	if isinstance(var, (types.FunctionType)):
		pass
	elif isinstance(var, (list, tuple, np.ndarray)):
		var=interp1d(x,var)
	else:
		raise RuntimeError('var must be a function, a list, a tuple, or an ndarray')

	#check if sampling is uniform:
	if abs(np.max(np.diff(x))-np.min(np.diff(x)))<0.000001*np.diff(x)[0]:
		dx=np.diff(x)[0]
	else:
		raise RuntimeError('Sampling must be uniform.')

	#build the new sampling array. Start at first element in x, end after we reach the last element in x:
	x_new=[x[0]]
	n=0

	m=np.max(var(x))

	#promt from gpt
	#Think of it like laying down footprints where your step size changes depending on the slope of the ground. 
	# If the slope is steep (narrow kernel → more detail), take small steps (high resolution). 
	# On flat ground (wide kernel → smooth area), take longer strides (less detail)
	while x_new[n]+var(x_new[n])/m/oversample*dx<=x[-1]:
		x_new.append(x_new[n]+var(x_new[n])/m/oversample*dx) #x_(n+1) = x_n + v(x_n)/(m*oversample) * dx
		n+=1
	x_new.append(x_new[n]+var(x_new[n])/m/oversample*dx) #last computation for x_new

	# There are two x axis here, x_new which is non-uniform and x which is uniform

	if len(kernel(m*oversample/dx))>len(x_new): # just a check for the kernel function to not be greater than the new x axis which will build the new interp signal, does nothing otherwise.
		raise RuntimeError('Kernel is larger than the data range.')

	y_new=np.interp(x_new,x,y) #Interpolates the new x data with the original signal function. 
	
	y_con=np.convolve(y_new,kernel(m*oversample/dx),mode=mode) #Convolves the new interpolated signal function with the kernel function.
	
	y_out=np.interp(x,x_new,y_con) #Another interp that I think creates y values on a non warped x axis

	"""
	Overall I think the way the convolve is working is by changing the resolution of the axies by stretching the x axis then resampling with the original x and y data.
	So even though its using a simple convolve, by how convolutions depend on dx or resolution the convolution will have a stronger influence where the x_new has a diff that 
	is much smaller than other parts. Refer to chatGPT_Varconvolve_Plot_Info.png for a plot of x_new. 
	chatGPT claims that this is a simplification rather than what is called "space-varying convolution". Im going to look into space-varying convolution as I think that is 
	what we are attempting.
	The final interp is so that the y values will align with the origianl x axis. May just make it easier to work with later if a uniform x axis is needed.
	"""
	
	return y_out#, y_con, y_new, x_new #returning everything generated to plot


def kernel(s):
	"""
	Constructs a normalized discrete 1D gaussian kernel
	"""
	size_grid = int(s*5)
	grid = np.mgrid[-size_grid:size_grid+1]

	g = np.exp(-(grid**2/float(s**2)/2.))
	return g / np.sum(g)

def var(x):
	"""
	Creates a polynomial that describes the kernel width
	"""
	p=[0.2,0.02]
	#print(np.polyval(p,x))
	return np.polyval(p,x)

#x sampling:
x=np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
#a delta function:
y=np.array([0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0])
#a step function that describes the kernel width:
v=np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.5,0.5,0.5]) # as the "width" increases the signal will be smeared more


#plot(x,y,'k-')
#y_c, y_c_Con, y_intN, x_new = varconvolve(x,y,kernel,var)
#y_cc, y_c_Con2, y_intN2, x_new2 = varconvolve(x,y,kernel,v)


#plot(x_new,y_intN)
#plot(x_new2,y_intN2)
#show()
#
#plot(x_new,y_c_Con,color="red")
#plot(x_new2,y_c_Con2,color="blue")
#show()
#
#plot(x,y_c,'r-')
#plot(x,y_cc,'b-')
#
#show()
