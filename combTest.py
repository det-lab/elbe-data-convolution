import numpy as np
import primaryConvolve as na
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import dataPull as dataP

fig = plt.figure(layout="constrained")


x = dataP.uniformNeutronEnergyList

# Parameters for the Gaussian comb
A = 20        # Amplitude
d = 1      # Distance between peaks
sigmaDiv = 0.05 # Standard deviation (width) of each Gaussian
N = 2000       # Number of terms in the summation on each side of the center



# Sum over the Gaussian functions
def combGaussian(xAxis, amp, distance, sigma, num):
    # Initialize the function
    F_x = np.zeros_like(x)
    for i in range(-num, num + 1):
        F_x += amp * np.exp(-((xAxis - i * distance)**2) / (2 * sigma**2))
    return(F_x)

controlPlot = np.array(combGaussian(x, 20, 1, 0.01, 200))

testPlot = na.convolution_2d_changing_kernel(controlPlot, dataP.matrixGaussian, x)
#testPlot2 = na.convolution_2d_changing_kernel(combGaussian(x, 20,0.5, 0.005, 200), ga.matrixGaussian, x)


gs = GridSpec(2,2, figure = fig)
ax1 = fig.add_subplot(gs[0,0:])
ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[1,1])

ax1.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'lightblue', linewidth = 3)
ax1.plot(x, testPlot, label='Convolved Gaussian Comb', color = "indigo")

ax2.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'lightblue', linewidth = 3)
ax2.plot(x, testPlot, label='Convolved Gaussian Comb', color = "indigo")
ax2.set_xlim(0.8,1.2)

ax3.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'lightblue', linewidth = 3)
ax3.plot(x, testPlot, label='Convolved Gaussian Comb', color = "indigo")
ax3.set_xlim(10.8,11.2)

fig.suptitle("GridSpec")

plt.show()
