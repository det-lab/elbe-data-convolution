import numpy as np
import pandas as pd
import os

#Imports the data from the excel file to make it avaliable for other programs

folder = 'data'

filename = 'LabFrameEnergyData.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print("reading file... " + file_path)
print("Computating Convolution")

neutronEnergy = pd.read_excel(file_path, usecols="E", header=0)
print(neutronEnergy)
theoryValues = pd.read_excel(file_path,usecols="B", header=0)
experemntValues = pd.read_excel(file_path,usecols="C", header=0)
uncertainty = pd.read_excel(file_path,usecols="D", header=0)

neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()

theoryValuesList = theoryValues["Theory function"].tolist()

neutronEnergyList = np.array(neutronEnergyList)

uniformNeutronEnergyList = np.linspace(neutronEnergyList[0], neutronEnergyList[-1], len(neutronEnergyList) * 2)

interpTheory = np.interp(uniformNeutronEnergyList, neutronEnergyList, theoryValuesList)

#Function that calculates the diviation for the gaussian function
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


#Returns a gaussian function with an axis of energy dependance, being centered on a specific energy level
def gaussian(energy , energyList):
    newGaussian = np.exp((((energy - energyList)**2))/(sigma(energy)**2) / (-2)) / (sigma(energy) * np.sqrt(2 * np.pi)) 

    steps = np.diff(energyList)
    integral = 0

    for value,step in zip(newGaussian,steps):

        integral += step*value
        
    return newGaussian / integral

#function that calculates the 2d matrix of all gaussian functions
matrixGaussian = []
for energy in uniformNeutronEnergyList:
    matrixGaussian.append(gaussian(energy, uniformNeutronEnergyList))

matrixGaussian = np.array(matrixGaussian)
