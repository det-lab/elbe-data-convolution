import numpy as np
import matplotlib.pyplot as plt
import dataPull as dataP
import primaryConvolve as na
import azureComparePython as azurePlots


#this program is usefull for conceptualizing how the gaussian is changing with energy
#keep in mind the values that are greater than zero are used in the convolution with the theory data

###Imports the variables from dataPull.py
expereimentValues = dataP.expereimentValues
uncertainty = dataP.uncertainty
neutronEnergyList = dataP.neutronEnergyList
theoryValuesList = dataP.theoryValuesList
neutronEnergyList = np.array(neutronEnergyList)
#creates a uniform energy axis inorder to ensure gaussian is normalized
uniformNeutronEnergyList = dataP.uniformNeutronEnergyList
interpTheory = dataP.interpTheory
interpExperimental = dataP.interpExperiment
#imports the 2d Gaussian matrix from dataPull.py
matrixGaussian = dataP.matrixGaussian
###

#uses the convolv function in newApproach.py to caluculate the points at a specifc index for the 2d gaussian matrix
theoryPlotPoints = na.convolution_2d_changing_kernel(interpTheory, matrixGaussian, uniformNeutronEnergyList) 
expereimentPlotPoints = na.convolution_2d_changing_kernel(interpExperimental, matrixGaussian, uniformNeutronEnergyList)

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = neutronEnergyList
# plots the theory values from the excel doc
line, = ax.plot(uniformNeutronEnergyList, interpTheory, color = "blue")
# plots the theory values convolved with the gaussian matrix
ax.plot(uniformNeutronEnergyList, theoryPlotPoints, color = "black")
#plots the interped experimental data
ax.plot(uniformNeutronEnergyList, interpExperimental, color ="red")
#plots the experimental data convolved with the gaussian matrix
ax.plot(uniformNeutronEnergyList, expereimentPlotPoints, color= "green")

ax.plot(azurePlots.azureLabEnergy[1], azurePlots.azureCrossSec[1], color="purple")

ax.set_yscale('linear')

plt.show()