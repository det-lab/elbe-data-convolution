import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 

folder = 'data'

filename = 'LabFrameEnergyData.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print("reading file... " + file_path)

neutronEnergy = pd.read_excel(file_path, usecols="E", header=0)

def dopplerDiv(neutronEnergy):
    boltsman = (1.380649 * 10**(-27)/(1.602*10**-19)) * 10**(-6)#Converted from Joules/Kkelvin to MeV/Kelvin
    temp = 293.15 #K

    targetMass = 2.32 * 10 **(-23)
    neutronMass = 1.674 * 10 **(-27)    
    massRatio = targetMass/neutronMass

    return np.sqrt(((2 * boltsman * temp)/massRatio) * neutronEnergy)

dopplerDivList = neutronEnergy.apply(dopplerDiv)

mean = np.mean(neutronEnergy)

gaussianFunc = np.exp(-(neutronEnergy - mean)**2 / (2 * dopplerDivList**2)) / (dopplerDivList * np.sqrt(2 * np.pi))

print(dopplerDivList)

plt.plot(neutronEnergy, gaussianFunc)
plt.ylabel("Doppler Broadening Func")
plt.xlabel("Neutron Energy (MeV)")
plt.show()
