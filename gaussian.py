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

#function for simgma value in the gaussian function
def sigma(neutronEnergy):
    dfPath = 0.0349 #cm
    fPath = 867.75 #cm
    dTof = 0.2007  #*(10**(-7)) nanoseconds to centiseconds???
    tof = np.sqrt(1.008665/(2*(neutronEnergy)))*fPath 

    #returns a sigma value for an input of the neutron energy where tof is related to the energy as well
    return neutronEnergy * 2 * np.sqrt(((dfPath/fPath)**2) + (((dTof/tof))**2))

#list of sigma values
sigmaList = neutronEnergy.apply(sigma)

#mean of the x values or neutron energy
mean = np.mean(neutronEnergy)

#y axis as a gaussian function
gaussianFunc = np.exp(-(neutronEnergy-mean)**2 / (2 * sigmaList**2)) / (sigmaList * np.sqrt(2 * np.pi))

#plots the gaussian function with the x axis being the neutron energy
plt.plot(neutronEnergy, gaussianFunc, )
plt.ylabel("Gaussian Func")
plt.xlabel("Neutron Energy (MeV)")
plt.show()
