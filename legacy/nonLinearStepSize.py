import numpy as np
import matplotlib as plt
import convolFunc as cf
import gaussianAnim as ga
import primaryConvolve as na
import legacy.gaussian as gauss


energyValues = ga.neutronEnergyList

def nonLinearStep(energy, i):
    if (i + 1) >= len(energy):
        return energy[i] - energy[i - 1]
    else:
        return energy[i + 1] - energy[i]

for i in range(len(energyValues)):
    plotPoints = np.convolve(ga.theoryValuesList, gauss.newGaussian, mode = "same") * nonLinearStep(energyValues, i)

plt.plot( ga.neutronEnergyList, ga.theoryValuesList, color = "Blue")
plt.plot( ga.neutronEnergyList, plotPoints, color = "Black")
plt.show()


