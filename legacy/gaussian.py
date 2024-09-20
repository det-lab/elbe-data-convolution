import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

folder = 'data'

filename = 'LabFrameEnergyData.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print("reading file... " + file_path)

neutronEnergy = pd.read_excel(file_path, usecols="E", header=0)

theoryValues = pd.read_excel(file_path,usecols="B", header=0)
experemntValues = pd.read_excel(file_path,usecols="C", header=0)
uncertainty = pd.read_excel(file_path,usecols="D", header=0)

#print(theoryValues)

#negNeutronEnergy = -neutronEnergy
#
#totalEngergy = pd.concat([negNeutronEnergy, neutronEnergy], ignore_index=True)
#
#totalEngergy = totalEngergy.sort_values(by="Lab Frame Energy")

#function for simgma value in the gaussian function
def sigma(neutronEnergy):
    #mass = ((1.674 * 10 ** -27) * (1/(1.6*10**-19)) * (10**-6)) / ((2.98*10**8)**2)#mass energy in MeV

    mass = 939.5654133 #/ (299792458) ** 2 # MeV per C^2 = mass

    #print("this is mass" , mass)
    dfPath = 0.349 * 10 ** -2 #cm to m

    fPath = 867.75 * 10 ** -2 #cm to m

    dTof = 0.2007  * (10 ** (-9)) #nanoseconds to seconds
    #print("This is neutron energy",neutronEnergy)
    # tof calculated with sqrt(mass/2Eng)*fpath
    tof = np.sqrt((mass)/(2*(neutronEnergy)))*fPath / (299792458) #Speed of light
    # sqrt((mev/c^2)/mev)*m = m/c = m/(m/s)
    #print("this is tof", tof)
    #returns a sigma value for an input of the neutron energy where tof is related to the energy as well
    return neutronEnergy * 2 * np.sqrt(((dfPath/fPath)**2) + (((dTof/tof))**2))


#list of sigma values
sigmaDataFrame = neutronEnergy.apply(sigma)
sigmaList = sigmaDataFrame["Lab Frame Energy"].tolist()

neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()

theoryValuesList = theoryValues["Theory function"].tolist()


#### Extreamly taxing code And Legacy Code ####

#for i in range(len(sigmaList)):
#    sigmaValue = sigmaList[i]
#
#    x_value = np.linspace(neutronEnergyList[i] - 0.01, neutronEnergyList[i] + 0.01, 200)
#    gaussianFuncProto = np.exp(((x_value - neutronEnergyList[i])**2)/(sigmaValue**2) / (-2)) / (sigmaValue * np.sqrt(2 * np.pi))
#    plt.plot(x_value, gaussianFuncProto)
#    #print(x_value - neutronEnergyList[i])
#    #print(2 * (pointer**2))
#    #print("gaussian Max Value at", i, np.exp(((x_value - neutronEnergyList[i])**2)/(pointer**2) / (-2)))

#### ####


uncertaintyList = uncertainty["Uncertainty"].tolist()

print(uncertaintyList[0])

userNeutronEnergy = input("Select input from 0 - 3680\n")

userNeutronEnergy = int(userNeutronEnergy)


# rewrite so calculates guassian points at neutron energy values instead of around user inputs

x_value = np.linspace(neutronEnergyList[userNeutronEnergy] - 0.01, neutronEnergyList[userNeutronEnergy] + 0.01, 28)

sigmaValue = sigmaList[userNeutronEnergy]

stepSize = x_value[1]-x_value[0]


mean = np.mean(neutronEnergyList)

#print(x_value)
gaussianFuncProto = np.exp((((mean - neutronEnergyList)**2))/(sigmaValue**2) / (-2)) / (sigmaValue * np.sqrt(2 * np.pi)) 

experemntValuesList = experemntValues["Experimental data"].tolist()

#print(gaussianFuncProto)

#interpolation of gaussian#

interpEnergy = np.linspace(neutronEnergyList[0], neutronEnergyList[-1], len(neutronEnergyList) * 20)

#newGaussian = np.interp(interpEnergy, neutronEnergyList, gaussianFuncProto)

print(np.size(neutronEnergyList))
print(np.size(theoryValuesList))

mean = np.mean(interpEnergy)

# changed from min of the sigma list to calculating new sigmas for every energy of interp

newGaussian = np.exp((((mean - interpEnergy)**2))/(sigma(interpEnergy)**2) / (-2)) / (sigma(interpEnergy) * np.sqrt(2 * np.pi)) 

interpTheory = np.interp(interpEnergy, neutronEnergyList, theoryValuesList) 

areaUnderGaus = sum(newGaussian) * (interpEnergy[2] - interpEnergy[1])

print("Area Under Gauss:", areaUnderGaus)

#non_zero_indices = [index for index, num in enumerate(newGaussian) if num != 0]
#energyInterval = interpEnergy[non_zero_indices]

plt.plot(neutronEnergyList, gaussianFuncProto, color="black")
plt.plot(interpEnergy, newGaussian, color = "red")
plt.show()

#gaussianReso = newGaussian[non_zero_indices]

stepSize = interpEnergy[2] - interpEnergy[1]

print("Step Size of Interp:", stepSize)

convovled = np.convolve(interpTheory , newGaussian , mode="same") * stepSize / areaUnderGaus

print(convovled)

#plt.plot(neutronEnergyList, theoryValuesList, color = "orange")
##plt.errorbar(neutronEnergyList, experemntValuesList, yerr = uncertaintyList, fmt="o",capsize = 5, color = "red")
#
#plt.plot(neutronEnergyList, convovled, color="blue")
plt.xlabel("Neutron Energy MeV")

plt.plot(interpEnergy, interpTheory, color = "blue")

plt.plot(interpEnergy, convovled, color = "black")
plt.grid()
plt.show()


#11.701
#0.105
#function for convovling resolution with theory values

#Legacy Code

#print("sigma Pick at 2", sigmaList)
#x_values = np.linspace(0.08, .11, 1000)
##y axis as a gaussian function
#gaussianFunc = np.exp(-(neutronEnergy ** 2) / (2 * sigmaList**2)) / (sigmaList * np.sqrt(2 * np.pi))
## expression of the gaussianFunc = e^(-MeV^2 / 2* MeV ^ 2) / (Mev * sqrt(2pi))
##print("this is gaussian values", gaussianFunc)
#
#
#
##plots the gaussian function with the x axis being the neutron energy
##plt.plot(neutronEnergy, sigmaList)
#plt.plot(x_values, gaussianFunc)
#plt.ylabel("Gaussian Func")
#plt.xlabel("Neutron Energy (MeV)")
#plt.show()
##print(totalEngergy.sort_values(by="Lab Frame Energy"))
##print(negNeutronEnergy)
##print(neutronEnergy)



# things for this week
# interpolate 