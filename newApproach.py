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
    
    stripedKernelMatrix = []

     # Initialize the output array
    output_length = len(signal)
    output = np.zeros(output_length)

    energyStepsList = np.diff(neutronEnergyList)
    energyStep = energyStepsList[1]
    checkLength= 0
    paddingConstant = 0
    
    for i, kernel_1d in enumerate(rawKernel):
        #Strips excess zeros from kernel
        kernel = [kernel for kernel in kernel_1d if kernel != 0]  
        stripedKernelMatrix.append(kernel)

        #checks to see if stripped kernel is longer than current padding constant
        if len(stripedKernelMatrix[i]) >= checkLength:
            checkLength = len(stripedKernelMatrix[i])
            paddingConstant = len(stripedKernelMatrix[i]) // 2
        #[0,0,0,0,0,0,0,0,2,4,2,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,2,5,6,7,6,5,2,0,0,0,0,0,0]
        #[2,4,2] pad length is 3
        #[2,5,6,7,6,5,2] pad length is 7
        #causes padding of first to be 
        #[0,0,2,4,2,0,0]
        #[0,0,2,5,6,7,6,5,2,0,0]
        #
        #(11-7) = 4
        #7-3
    
    for i, kernel_1d in enumerate(stripedKernelMatrix):
        deltaLength = checkLength - len(kernel_1d)
        

        #pads every gaussian in the stripped matrix to be of the constant padding
        stripedKernelMatrix[i] = np.pad(kernel_1d, (paddingConstant + deltaLength, paddingConstant + deltaLength), "constant")
        #if (len(stripedKernelMatrix[i]) != checkLength):
        #    print("Incorrect dim at lenght", len(stripedKernelMatrix[i]))
        #    print(len(np.pad(signal, (paddingConstant, paddingConstant), 'constant')))



    for i, kernel in enumerate(stripedKernelMatrix):

        ## Flip the kernel
        #kernel = np.flip(kernel)
#
        ## Calculate the padding needed
        #pad_left = len(kernel) // 2
        #pad_right = len(kernel) // 2
#
        #if pad_left != int or pad_right != int:
        #    round(pad_left)
        #    round(pad_right)

        # Pad the signal with zeros on both ends
        padded_signal = np.pad(signal, (paddingConstant, paddingConstant), 'constant')
        print("Length of kernel: ", len(kernel))
        print("Length of padded signal: ", len(padded_signal[i:i + len(kernel)]))
        # Perform the convolution operation
        
        if len(padded_signal[i:i + len(kernel)]) == len(kernel):
            output[i] = np.sum(padded_signal[i:i + len(kernel)] * kernel) * energyStep
        

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
