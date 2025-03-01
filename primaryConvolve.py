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

def convolution_1and2D(signal, kernel, axis, inputFunc,mode):
    
    sortArry = kernel.ndim

    if sortArry == 1:
        kernel = kernel[::-1]  # Reverse kernel for convolution
        output = []

        for i in range(1 - len(kernel), len(signal)):  # Slide kernel across signal

            start = max(0, i)
            # max(0, -3)
            end = min(i + len(kernel), len(signal))
            # min(-3 + 4, 5)
            kernel_start = max(-i, 0)
            # max(3, 0)
            kernel_end = kernel_start + (end - start)
            # 3 + (1 - 0) = 4

            conv_result = np.dot(signal[start:end], kernel[kernel_start:kernel_end])
            # signal[0:1], kernel[3:4]
            # signal[0:2], kernel[2:4]
            output.append(conv_result) #appends the full convolution

        #### Convolution has already been done, just formating below ####

        if mode == "same": #if same is passed into function, the "full" convolution is then cut down to be same dim as the signal array
            sliceIndex = (len(kernel) - 1)//2 # How much to slice off the ends of the output is based on the length of the kernel

            if len(kernel) % 2 == 0:
                output = output[sliceIndex:-(sliceIndex+1)] # To follow python, cutting one extra during an even sized kernel
                print("kernel is Even")
            else: 
                output = output[sliceIndex:-(sliceIndex)] # If odd, nother special is need in slicing
                print("Kernel is Odd")
            return output
        else: return output

    
    elif sortArry == 2:

        output = []
        

        #for indivKernel in kernel:
        #    indivKernel = [num for num in indivKernel if num != 0] #strips zeros from the function
        


        for i in range(1 - len(kernel), len(signal)):  # Slide kernel across signal
            
            start = max(0, i)
            # max(0, -3)
            end = min(i + len(kernel), len(signal))
            # min(-3 + 4, 5)
            kernel_start = max(-i, 0)
            # max(3, 0)
            kernel_end = kernel_start + (end - start)
            # 3 + (1 - 0) = 4
            
            conv_result = np.dot(signal[start:end], kernel[start][kernel_start:kernel_end])
            # signal[0:1], kernel[3:4]
            # signal[0:2], kernel[2:4]
            
            output.append(conv_result) #appends the full convolution

        #### Convolution has already been done, just formating below ####

        if mode == "same": #if same is passed into function, the "full" convolution is then cut down to be same dim as the signal array
            sliceIndex = (len(kernel) - 1)//2 # How much to slice off the ends of the output is based on the length of the kernel

            if len(kernel) % 2 == 0:
                output = output[sliceIndex:-(sliceIndex+1)] # To follow python, cutting one extra during an even sized kernel
                print("kernel is Even")
            else: 
                output = output[sliceIndex:-(sliceIndex)] # If odd, nother special is need in slicing
                print("Kernel is Odd")
            return output
        else: return output


        """
        np.flip(kernel)
        pad_left = len(kernel) 
        pad_right = len(kernel) 

        signal = np.pad(signal, (pad_left, pad_right), 'constant')

        output_length = len(signal)
        output = np.zeros(output_length)

        for i in range(output_length):

            output[i] = np.sum(signal[i:i + len(kernel)] * kernel[i] ) * deltaAxis

        return output
        """