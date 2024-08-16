import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numba import jit
import newApproach as na


#this program is usefull for conceptualizing how the gaussian is changing with energy
#keep in mind the values that are greater than zero are used in the convolution with the theory data


folder = 'data'

filename = 'LabFrameEnergyData.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print("reading file... " + file_path)
print("Computating Convolution")

neutronEnergy = pd.read_excel(file_path, usecols="E", header=0)

theoryValues = pd.read_excel(file_path,usecols="B", header=0)
experemntValues = pd.read_excel(file_path,usecols="C", header=0)
uncertainty = pd.read_excel(file_path,usecols="D", header=0)


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


#list of sigma values and creating lists for excel data
sigmaDataFrame = neutronEnergy.apply(sigma)
sigmaList = sigmaDataFrame["Lab Frame Energy"].tolist()

neutronEnergyList = neutronEnergy["Lab Frame Energy"].tolist()

theoryValuesList = theoryValues["Theory function"].tolist()

neutronEnergyList = np.array(neutronEnergyList)

uniformNeutronEnergyList = np.linspace(neutronEnergyList[0], neutronEnergyList[-1], len(neutronEnergyList) * 2)

interpTheory = np.interp(uniformNeutronEnergyList, neutronEnergyList, theoryValuesList) 

# changed from min of the sigma list to calculating new sigmas for every energy of interp, might be what we are looking for
def gaussian(energy , energyList):
    newGaussian = np.exp((((energy - energyList)**2))/(sigma(energy)**2) / (-2)) / (sigma(energy) * np.sqrt(2 * np.pi)) 

    steps = np.diff(energyList)
    integral = 0

    for value,step in zip(newGaussian,steps):

        integral += step*value
        
    return newGaussian / integral

#for i in range(len(gaussian(1))):
#    if gaussian(index)[i] > 0:
#        print("newGaussian value is:", gaussian[i], "\n", "At index:", i)
#    
#plt.plot(interpEnergy, newGaussian, color = "Black")
#plt.show()

#function that calculates the 2d matrix of all gaussian functions
matrixGaussian = []
for energy in uniformNeutronEnergyList:
    matrixGaussian.append(gaussian(energy, uniformNeutronEnergyList))

matrixGaussian = np.array(matrixGaussian)

#picks a specific gaussian array from the 2d matrix
currentArray = matrixGaussian[4000]


#newCurrentArray = [newCurrentArray for newCurrentArray in currentArray if newCurrentArray != 0]

#uses the convolv function in newApproach.py to caluculate the points at a specifc index for the 2d gaussian matrix
plotPoint = na.convolution_2d_changing_kernel(interpTheory, matrixGaussian, uniformNeutronEnergyList) 

#troubleshooting

#performs a numpy convolution to be compared with the custom method
numpyConvolve = np.convolve(currentArray, interpTheory, mode = "same")

#rounds both arrays for the next step of checking, if not rounded they will trip the check at a very low decimal place
numpyConvolveRoundCheck = np.round(numpyConvolve,8)
plotPointRoundCheck = np.round(plotPoint,8)

#performs a check for equivilence 
#for i in range(len(plotPoint)):
#    if numpyConvolveRoundCheck[i] != plotPointRoundCheck[i]:
#        print("Does not match Numpy conv at index:", i)

#Start of normalization of the plot points
#stepArray = []
#for i in range(len(neutronEnergyList)):
#    if (1+i) >= len(matrixGaussian):
#        stepSize = neutronEnergyList[i] - neutronEnergyList[i-1]
#    else:
#        stepSize = neutronEnergyList[1 + i] - neutronEnergyList[i]
#    stepArray.append(stepSize)

def normalization(values, energy, index):

    values = np.array(values)

    if len(energy) <= (index + 1):
        stepSize = energy[index] - energy[index - 1]
    else:
        stepSize = energy[index + 1] - energy[index] 

    area = np.trapz(values, energy)

    valuesNormalized = (values * stepSize)/area
    return valuesNormalized

def normalize_matrix(matrix):
    # Convert the matrix to a NumPy array if it's not already
    matrix = np.array(matrix)
    
    # Calculate the sum of all elements in the matrix
    total_sum = np.sum(matrix)
    
    # Normalize the matrix so that the sum of all elements equals 1
    if total_sum != 0:  # To avoid division by zero
        normalized_matrix = matrix / total_sum
    else:
        normalized_matrix = matrix  # If the sum is zero, return the matrix as is (though it would be all zeros)
    
    return normalized_matrix

#Begins to plot the points for all gaussians in the 2d matrix
def NormPlot():
    #declares the final array of points
    finalPlotArray = []
    normInputMatrix = normalize_matrix(matrixGaussian)
    #for loop that computes the points of the energy changing convolution
    for i in range(len(neutronEnergyList)):

        if (i + 1) >= len(neutronEnergyList):
            stepSize = neutronEnergyList[i] - neutronEnergyList[i - 1]
        else:
            stepSize = neutronEnergyList[i + 1] - neutronEnergyList[i]


        currentConv = na.convolution_1d_same(theoryValuesList, normInputMatrix[400]) 
        #normCurrentConv = normalization(currentConv, neutronEnergyList, i)
        finalPlotArray.append(currentConv)

    return finalPlotArray

#holdFullPlot = 

#finalPlot = NormPlot()

# Set up the figure, axis, and plot element we want to animate
fig, ax = plt.subplots()
x = neutronEnergyList
energy = neutronEnergyList[0]
line, = ax.plot(x, gaussian(energy, neutronEnergyList), color = "white")
ax.plot(neutronEnergyList, theoryValuesList, color = "blue")
ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[200],  uniformNeutronEnergyList), color="red")
ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[850], uniformNeutronEnergyList), color="orange")

ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[1500], uniformNeutronEnergyList), color="lawngreen")
ax.plot(uniformNeutronEnergyList, plotPoint, color = "black")

#ax.plot(uniformNeutronEnergyList, interpTheory, color = "green")

#ax.plot(x, np.linspace(2000,2000, len(x)), color = "blue")

ax.set_yscale('log')
ax.set_ylim(0.01, 6000)

# Initialization function: plot the background of each frame
def init():
    energy = neutronEnergyList[0]
    line.set_ydata(gaussian(energy, neutronEnergyList))
    return line,

# Animation function: this is called sequentially
def update(frame):
    energy = neutronEnergyList[0 + frame]
    line.set_ydata(gaussian(energy, neutronEnergyList))  # Update the data
    return line,

# Call the animator
ani = animation.FuncAnimation(
    fig, update, frames=len(neutronEnergyList), init_func=init, blit=True, interval=1,)

# Define the pause/resume functionality
is_paused = [False]  # Use a list to allow modification in the event handler

def on_key_press(event):
    if event.key == 'p':  # Press 'p' to pause/resume the animation
        if is_paused[0]:
            ani.event_source.start()
        else:
            ani.event_source.stop()
        is_paused[0] = not is_paused[0]

# Connect the event handler to the figure
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Show the animation
plt.show()



###Old Code Ignore for now###

#Checks for values that are non zero in a specific gaussian
#for i in range(len(matrixGaussian[400])):
#    currentArray = matrixGaussian[400]
#    if currentArray[i] != 0:
#        print("non zero at index:", i)


#for loop that caculates the product sum of theory and gaussian values
#for i in range(len(matrixGaussian)):
#    currentGaus = matrixGaussian[i]
#    sumPoint = 0
#    #r = np.convolve(neutronEnergyList, currentGaus,mode="same")
#    #sumPoint = r[i]
#    for j in range(len(currentGaus)):
#        if currentGaus[j] != 0 and neutronEnergyList[j] !=0:
#            sumPoint += currentGaus[j]*neutronEnergyList[j]
#    
#    #Changes step size for each normalization 
#    if (1+i) >= len(matrixGaussian):
#        stepSize = neutronEnergyList[i] - neutronEnergyList[i-1]
#    else:
#        stepSize = neutronEnergyList[1 + i] - neutronEnergyList[i]
#
#    sumPoint = sumPoint * stepSize
#    plotPoint.append(sumPoint)

#calculates step size for graph