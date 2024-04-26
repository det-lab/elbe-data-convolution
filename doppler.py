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

#Function to calculate doppler deviation
def dopplerDiv(neutronEnergy):
    boltsman = (1.380649 * 10**(-23)/(1.602*10**-19))#Converted from Joules/kelvin to eV/Kelvin
    boltsman = boltsman * 10**(-6) #convert eV/Kelvin to MeV/Kelvin
    temp = 293.15 #K

    targetMass = 14.003 # Mass of N14 in Amu
    neutronMass = 1.008 # Mass in Amu   
    massRatio = targetMass/neutronMass

    return np.sqrt(((2 * boltsman * temp)/massRatio) * neutronEnergy)

#applys the doppler function to each value of neutron energy returning a specific deviation
dopplerDivFrame = neutronEnergy.apply(dopplerDiv)

#converts data frames to list for more simple manipulation
dopplerDivList = dopplerDivFrame["Lab Frame Energy"].tolist()
neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()


#Function that plots points with a range of domain values
for n, d in zip(neutronEnergyList,dopplerDivList):
    x_values = np.linspace(n - 0.01, n +0.01, 10)
    y_value = np.exp((-( x_values- n )**2 / (d**2))/(2)) / (d * np.sqrt(2 * np.pi))
    print(y_value)
    plt.plot(x_values,y_value)
plt.ylabel("Doppler Broadening Func")
plt.xlabel("Neutron Energy (MeV)")
plt.show()


#redfined vars to make following operation "readable"
n = neutronEnergyList
d = dopplerDivList

#Creates a list of y values where the shift is zero
y_value = [np.exp((-( 0 )**2 / (d**2))/(2)) / (d * np.sqrt(2 * np.pi)) for n, d in zip(neutronEnergyList,dopplerDivList)]

    
plt.plot(neutronEnergyList, y_value)
plt.show()

#x_values = np.linspace(neutronEnergyList[300]- 0.01, neutronEnergyList[300]+0.01, 200)

#print(x_values)
#mean = np.mean(neutronEnergy)

#print(-(-x_values - neutronEnergyList[300])**2 / (2 * dopplerDivList**2))

#gaussianFunc = np.exp((-(x_values- neutronEnergyList[300])**2 / (dopplerDivList[300]**2))/(2)) / (dopplerDivList[300] * np.sqrt(2 * np.pi))

#print(dopplerDivList)
#print(-(neutronEnergy)**2 / (2 * dopplerDivList**2))

#plt.plot(x_values, y_value(dopplerDivList, neutronEnergyList))
#plt.ylabel("Doppler Broadening Func")
#plt.xlabel("Neutron Energy (MeV)")
#plt.show()
