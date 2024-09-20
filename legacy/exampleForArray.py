import numpy as np
import newApproach as na

amatrix = []

#creates 2d matrix
for i in range(11):
    current = np.linspace(1,20,i)
    amatrix.append(current)


#example signal
signal = (np.sin(np.linspace(0,2*np.pi))**2)

#finds the max pad constant
for i in range(len(amatrix)):
    if len(amatrix[i]) > len(amatrix[i-1]):
        constant = len(amatrix)

#pads the signal
pad_signal = np.pad(signal,(constant, constant), "constant" )

#defines the output len
output = np.linspace(0,0,len(signal))


for i, k in enumerate(amatrix):
    output[i] = np.sum(pad_signal[i:i + len(k)] * k)

xAxis = [1,2,3,4,5,6,7,8,9,10,11,12,13]

signal = [2,5,2,5,2,5,2,5,2,5,2,5,2]

arrayKern = [
[2,2,0,0,0,0,0,0,0,0,0,0,0],
[4,2,0,0,0,0,0,0,0,0,0,0,0],
[2,4,4,2,0,0,0,0,0,0,0,0,0],
[0,2,4,4,2,0,0,0,0,0,0,0,0],
[0,0,2,4,5,4,2,0,0,0,0,0,0],
[0,0,0,2,4,5,5,2,0,0,0,0,0],
[0,0,0,0,2,4,7,9,7,4,2,0,0],
[0,0,0,0,0,0,2,4,7,9,7,4,2],
[0,0,0,0,0,0,0,2,4,7,9,7,4],
[0,0,0,0,0,0,0,0,2,4,7,9,7],
[0,0,0,0,0,0,0,0,0,2,4,7,9],
[0,0,0,0,0,0,0,0,0,0,2,4,7],
[0,0,0,0,0,0,0,0,0,0,0,2,4]
]

na.convolution_2d_changing_kernel(signal, arrayKern, xAxis)


#for i, kernel_1d in enumerate(array):
#    #Strips excess zeros from kernel
#    kernel = [kernel for kernel in kernel_1d if kernel != 0]  
#    stripedKernelMatrix.append(kernel)
#
#    if len(stripedKernelMatrix[i]) >= checkLength:
#        checkLength = len(stripedKernelMatrix[i])
#        paddingConstant = len(stripedKernelMatrix[i]) // 2
#
#print(stripedKernelMatrix)
#print(paddingConstant)
