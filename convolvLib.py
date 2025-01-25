import numpy as np

#kernel function needs to be a function of the axis

def sigma(neutronEnergy):
    #mass = ((1.674 * 10 ** -27) * (1/(1.6*10**-19)) * (10**-6)) / ((2.98*10**8)**2)#mass energy in MeV

    mass = 939.5654133 #/ (299792458) ** 2 # MeV per C^2 = mass

    #print("this is mass" , mass)
    dfPath = 0.349 * 10 ** -2 #cm to m

    fPath = 867.75 * 10 ** -2 #cm to m

    dTof = 0.2007  * (10 ** (-9)) #nanoseconds to seconds
    
    # tof calculated with sqrt(mass/2Eng)*fpath
    tof = np.sqrt((mass)/(2*(neutronEnergy)))*fPath / (299792458) #Speed of light
    
    #returns a sigma value for an input of the neutron energy where tof is related to the energy as well
    return neutronEnergy * 2 * np.sqrt(((dfPath/fPath)**2) + (((dTof/tof))**2))


#Returns a gaussian function with an axis of energy dependance, being centered on a specific energy level
def kernel(energy , energyList):
    
    newGaussian = np.exp((((energy - energyList)**2))/(sigma(energy)**2) / (-2)) / (sigma(energy) * np.sqrt(2 * np.pi)) 

    #delta of the energy list used in the intergral calculation
    #note that the energy list in the data is not uniform
    deltaEnergy = np.diff(energyList)
    integral = 0

    #For loop to normalize the gaussian to an area of 1
    for value,dE in zip(newGaussian,deltaEnergy):
        
        #takes the gaussian and multiplies it by the step size to form a normalization
        integral += dE*value
        
    #returns the gaussian normalized with the area under the gaussian
    return newGaussian / integral



def convolve2D(kernel, dataSet, axis):
    #forms array for output
    output_length = len(dataSet)
    output = np.zeros(output_length)

    #Change in axis for normalization
    deltaAxis = np.diff(axis)
    deltaAxis = np.append(deltaAxis, deltaAxis[-1])

    matrixKernel = []
    for x in axis:
        matrixKernel.append(kernel(x, axis)) #in general case, requires that the function is fliped, however does not play nice with arrays 
    matrixKernel = np.array(matrixKernel)

    for i, f in enumerate(matrixKernel):
        #sums the the 1d arrays to return a single value to then be appended to the convolved array output
        output[i] = np.sum((dataSet * f) * deltaAxis)
    return output


