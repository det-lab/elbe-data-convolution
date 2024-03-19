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

#negNeutronEnergy = -neutronEnergy
#
#totalEngergy = pd.concat([negNeutronEnergy, neutronEnergy], ignore_index=True)
#
#totalEngergy = totalEngergy.sort_values(by="Lab Frame Energy")

#function for simgma value in the gaussian function
def sigma(neutronEnergy):
    #mass = ((1.674 * 10 ** -27) * (1/(1.6*10**-19)) * (10**-6)) / ((2.98*10**8)**2)#mass energy in MeV

    mass = 939.5654133 #/ (299792458) ** 2 # MeV per C^2 = mass

    print("this is mass" , mass)
    dfPath = 0.349 * 10 ** -2 #cm to m

    fPath = 867.75 * 10 ** -2 #cm to m

    dTof = 0.2007  * (10 ** (-9)) #nanoseconds to seconds
    print("This is neutron energy",neutronEnergy)
    # tof calculated with sqrt(mass/2Eng)*fpath
    tof = np.sqrt((mass)/(2*(neutronEnergy)))*fPath / (299792458)
    # sqrt((mev/c^2)/mev)*m = m/c = m/(m/s)
    print("this is tof", tof)
    #returns a sigma value for an input of the neutron energy where tof is related to the energy as well
    return neutronEnergy * 2 * np.sqrt(((dfPath/fPath)**2) + (((dTof/tof))**2))


#list of sigma values
#sigmaList = sigma(neutronEnergy.iat[2,0])
sigmaDataFrame = neutronEnergy.apply(sigma)
sigmaList = sigmaDataFrame["Lab Frame Energy"].tolist()
print("This is sigma List", sigmaList)
neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()
print("this is Neutron Energy List", neutronEnergyList)

for i in range(len(sigmaList)):
    pointer = sigmaList[i]

    x_value = np.linspace(neutronEnergyList[i] - 0.01, neutronEnergyList[i] + 0.01, 200)
    gaussianFuncProto = np.exp(((x_value - neutronEnergyList[i])**2)/(pointer**2) / (-2)) / (pointer * np.sqrt(2 * np.pi))
    plt.plot(x_value, gaussianFuncProto)
    print(x_value - neutronEnergyList[i])
    print(2 * (pointer**2))
    #print("gaussian Max Value at", i, np.exp(((x_value - neutronEnergyList[i])**2)/(pointer**2) / (-2)))

plt.show()


print("sigma Pick at 2", sigmaList[2])
x_values = np.linspace(0.08, .11, 1000)
#y axis as a gaussian function
gaussianFunc = np.exp(-(x_values - neutronEnergy.iat[2,0])**2 / (2 * sigmaList.iat[2,0]**2)) / (sigmaList.iat[2,0] * np.sqrt(2 * np.pi))
# expression of the gaussianFunc = e^(-MeV^2 / 2* MeV ^ 2) / (Mev * sqrt(2pi))
print("this is gaussian values", gaussianFunc[50])



#plots the gaussian function with the x axis being the neutron energy
#plt.plot(neutronEnergy, sigmaList)
plt.plot(x_values, gaussianFunc)
plt.ylabel("Gaussian Func")
plt.xlabel("Neutron Energy (MeV)")
plt.show()
#print(totalEngergy.sort_values(by="Lab Frame Energy"))
#print(negNeutronEnergy)
#print(neutronEnergy)