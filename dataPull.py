import numpy as np
import pandas as pd
import os
import azureComparePython as azurePlots

#Imports the data from the excel file to make it avaliable for other programs

folder = 'data'

filename = 'LabFrameEnergyData.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print("reading file... " + file_path)
print("Computating Convolution")

#imports all of the excel data into pandas arrays
neutronEnergy = pd.read_excel(file_path, usecols="E", header=0)
theoryValues = pd.read_excel(file_path,usecols="B", header=0)
expereimentValues = pd.read_excel(file_path,usecols="C", header=0)
uncertainty = pd.read_excel(file_path,usecols="D", header=0)

#converts pandas arrays into lists for ease of use
neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()
theoryValuesList = theoryValues["Theory function"].tolist()
expereimentValuesList = expereimentValues["Experimental data"].tolist()
neutronEnergyList = np.array(neutronEnergyList)

#for loop to reduce range of interp
def narrowingFunc():
    startIndex = int
    endIndex = int
    for i, values in enumerate(neutronEnergyList):
        if values >= azurePlots.azureLabEnergy[0]:
            
            startIndexNeutron = i
            break

    for i, values in enumerate(neutronEnergyList):
        if values >= azurePlots.azureLabEnergy[-1]:
            
            endIndexNeutron = i
            break
    
    neutronEnergyShortend = neutronEnergy[startIndexNeutron:endIndexNeutron]
    theoryShortend = theoryValuesList[startIndexNeutron:endIndexNeutron]

    return neutronEnergyShortend, theoryShortend

shortenListsArray = list(narrowingFunc())


shortenListsArray[0] = np.asarray(shortenListsArray[0]).flatten()
shortenListsArray[1] = np.asarray(shortenListsArray[1]).flatten()

shortNeutron = shortenListsArray[0]

#creates a new uniform list of energy values 
uniformNeutronEnergyList = np.linspace(shortNeutron[0],shortNeutron[-1], len(neutronEnergyList) * 2)

#creates interped values from uniform neutron energies
interpTheory = np.interp(uniformNeutronEnergyList, shortenListsArray[0], shortenListsArray[1])
interpExperiment = np.interp(uniformNeutronEnergyList, neutronEnergyList, expereimentValuesList)
print("Here", uniformNeutronEnergyList)

#Function that calculates the diviation for the gaussian function
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
def gaussian(energy , energyList):
    
    newGaussian = np.exp((((energy - energyList)**2))/(sigma(energy)**2) / (-2)) / (sigma(energy) * np.sqrt(2 * np.pi)) 

    #delta of the energy list used in the intergral calculation
    steps = np.diff(energyList)
    integral = 0

    #For loop to normalize the gaussian to an area of 1
    for value,step in zip(newGaussian,steps):
        
        #takes the gaussian and multiplies it by the step size to form a normalization
        integral += step*value
        
    #returns the gaussian normalized with the area under the gaussian
    return newGaussian / integral

#function that calculates the 2d matrix of all gaussian functions
# Referance picture 1 in physics photos
matrixGaussian = []
for energy in uniformNeutronEnergyList:
    matrixGaussian.append(gaussian(energy, uniformNeutronEnergyList))

matrixGaussian = np.array(matrixGaussian)
