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
matrixGaussian = dataP.matrixGaussianFunc(uniformNeutronEnergyList)
###

testMatrix = dataP.matrixGaussianFunc(neutronEnergyList)

testTheory = na.convolution_2d_changing_kernel(theoryValuesList, testMatrix, neutronEnergyList)


#uses the convolv function in newApproach.py to caluculate the points at a specifc index for the 2d gaussian matrix
theoryPlotPoints = na.convolution_2d_changing_kernel(interpTheory, matrixGaussian, uniformNeutronEnergyList)

#expereimentPlotPoints = na.convolution_2d_changing_kernel(interpExperimental, matrixGaussian, uniformNeutronEnergyList)

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
# plots the theory values from the excel doc
#line, = ax.plot(uniformNeutronEnergyList, interpTheory, color = "blue" , label ="Theory No Convolution", linewidth = 3)
# plots the theory values convolved with the gaussian matrix

#plots the interped experimental data
ax.plot(dataP.neutronEnergyList, dataP.expereimentValuesList,"o", color ="red" , label = "Experimental Data")

ax.plot(uniformNeutronEnergyList, theoryPlotPoints, color = "black" , label = "Python Based Convolution", linewidth = 2, marker = "x")

#plots the experimental data convolved with the gaussian matrix
#ax.plot(uniformNeutronEnergyList, expereimentPlotPoints, color= "green", label = "Experimental Convolution", linewidth = 2)

ax.plot(azurePlots.azureLabEnergy, azurePlots.azureCrossSec[3], color="green", label = "Azure Based Convoltion", linewidth = 2, marker = "x")

ax.plot(neutronEnergyList, testTheory, color = "blue", label="Test Plot")

ax.set_yscale('log')

plt.legend(loc="upper left", fontsize = 24)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel("Lab Frame Energy (MeV)",fontsize = 20)
plt.ylabel("Yield (Unit Less)",fontsize = 20)
plt.xlim(0.3, 0.5)


plt.show()