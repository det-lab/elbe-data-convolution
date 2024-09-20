import numpy as np
import matplotlib.pyplot as plt
import dataPull as dataP
import newApproach as na

#this program is usefull for conceptualizing how the gaussian is changing with energy
#keep in mind the values that are greater than zero are used in the convolution with the theory data

###Imports the variables from dataPull.py
experemntValues = dataP.experemntValues
uncertainty = dataP.uncertainty
neutronEnergyList = dataP.neutronEnergyList
theoryValuesList = dataP.theoryValuesList
neutronEnergyList = np.array(neutronEnergyList)
#creates a uniform energy axis inorder to ensure gaussian is normalized
uniformNeutronEnergyList = np.linspace(neutronEnergyList[0], neutronEnergyList[-1], len(neutronEnergyList) * 2)
interpTheory = np.interp(uniformNeutronEnergyList, neutronEnergyList, theoryValuesList) 
#imports the 2d Gaussian matrix from dataPull.py
matrixGaussian = dataP.matrixGaussian
###

#picks a specific gaussian array from the 2d matrix
currentArray = matrixGaussian[4000]

#uses the convolv function in newApproach.py to caluculate the points at a specifc index for the 2d gaussian matrix
plotPoint = na.convolution_2d_changing_kernel(interpTheory, matrixGaussian, uniformNeutronEnergyList) 

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = neutronEnergyList
line, = ax.plot(neutronEnergyList, theoryValuesList, color = "blue")
ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[200],  uniformNeutronEnergyList), color="red")
ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[850], uniformNeutronEnergyList), color="orange")

ax.plot(uniformNeutronEnergyList, na.convolution_1d_same(interpTheory, matrixGaussian[1500], uniformNeutronEnergyList), color="lawngreen")
ax.plot(uniformNeutronEnergyList, plotPoint, color = "black")

ax.set_yscale('log')
ax.set_ylim(0.01, 6000)

plt.show()