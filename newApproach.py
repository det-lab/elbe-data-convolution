import numpy as np

def convolution_1d_same(signal, rawKernel, neutronEnergyList):
    
    kernel = [kernel for kernel in rawKernel if kernel != 0]

    # Flip the kernel
    kernel = np.flip(kernel)

    # Calculate the padding needed
    pad_left = len(kernel) // 2
    pad_right = len(kernel) // 2

    if pad_left != int or pad_right != int:
        round(pad_left)
        round(pad_right)
    
    # Pad the signal with zeros on both ends
    padded_signal = np.pad(signal, (pad_left, pad_right), 'constant')
    
    # Initialize the output array
    output_length = len(signal)
    output = np.zeros(output_length)

    energyStepsList = np.diff(neutronEnergyList)
    energyStep = energyStepsList[1]

    # Perform the convolution operation
    for i in range(output_length):

        output[i] = np.sum(padded_signal[i:i + len(kernel)] * kernel ) * energyStep
    
    return output

def convolution_2d_changing_kernel(signal, rawKernel, neutronEnergyList):

     # Initialize the output array
    output_length = len(signal)
    output = np.zeros(output_length)

    energyStepsList = np.diff(neutronEnergyList)
    energyStep = energyStepsList[1]

    # Dot product of the signal and kernel, the kernel is already moving along the signal with the 2d raw kernel
    for i, kernel in enumerate(rawKernel):
        
        output[i] = np.dot(signal, kernel) * energyStep
        #takes the sum of the padded_signal with its length equal to that of the kernels
        
    print(output)
    return output

x = np.linspace(0, 200, 200)
y = np.linspace(0,10, 20)

diff = np.linspace(0,2, 2000)

#L1 = np.linspace(25,50,25)
#L2 = np.linspace(1,10,10)
#
#
#rArray = []
#
#def dataLoop():
#    
#    for i in range(1,len(L1)):
#        #print("I index is: ", i)
#        r = 0
#        for j in range(1,len(L2)):
#            
#            if (i-j) < 0:
#                
#                break
#            else: 
#                r += L1[i-j] * L2[-j]
#
#        rArray.append(r)
#
#    return rArray
#
#print(dataLoop())
#
#print(np.convolve(L2,L1, mode="full"))
#print(len(dataLoop()))
#print(len(np.convolve(L2,L1, mode="full")))
