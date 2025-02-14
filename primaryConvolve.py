import numpy as np

#Convolution of two 1d arrays
#[0,0,1,1,0,0]
#[2,3,4,2,5,3]
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

#convolution of 2d kernal array and signal
#{[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]}
#[2,3,4,2]
def convolution_2d_changing_kernel(signal, matrix2D, neutronEnergyList):

     # Initialize the output array
    output_length = len(signal)
    output = np.zeros(output_length)

    #Normilization of output, however is much more irrelivent now due to the step amount being constant
    energyStepsList = np.diff(neutronEnergyList)
    energyStepsList = np.append(energyStepsList, energyStepsList[-1])
    # Dot product of the signal and kernel, the kernel is already moving along the signal with the 2d raw kernel
    for i, kernel in enumerate(matrix2D):
        
        #sums the the 1d arrays to return a single value to then be appended to the convolved array output
        output[i] = np.sum(signal * kernel * energyStepsList)
    
    return output

def convolution_1and2D(signal, kernel, axis):
    
    sortArry = kernel.ndim

    deltaAxis = np.diff(axis)
    deltaAxis = deltaAxis[1]

    if sortArry == 1:
        
        axisIndex = len(axis)//2

        for i, array in enumerate(kernel[axisIndex:-1]):
            if array != 0:
                if array == 0:
                    leftOffset_Padding = (kernel[axisIndex + i - 1] // 2) * 10
                    break
            elif array == 0:
                leftOffset_Padding = 0
                break
        


        np.flip(kernel)
        pad_left = leftOffset_Padding + len(kernel)//2
        pad_right = len(kernel)//2

        signal = np.pad(signal, (pad_left, pad_right), 'constant')

        output_length = len(kernel)
        output = np.zeros(output_length)

        for i in range(output_length):
            print(i, "to", i + len(kernel))
            if len(signal[i:i + len(kernel)]) == len(kernel):
                output[i] = np.sum(signal[i:i + len(kernel)] * kernel ) * deltaAxis
            else:
                output[i] = 0
                print("Artifical 0 created at index", i, "due to improper array length")
        return output
    
    elif sortArry == 2:

        np.flip(kernel)
        pad_left = len(kernel) 
        pad_right = len(kernel) 

        signal = np.pad(signal, (pad_left, pad_right), 'constant')

        output_length = len(signal)
        output = np.zeros(output_length)

        for i in range(output_length):

            output[i] = np.sum(signal[i:i + len(kernel)] * kernel[i] ) * deltaAxis

        return output
