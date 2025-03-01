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

gaussianMatrix = dataP.matrixGaussianFunc(x)

# Sum over the Gaussian functions
def combGaussian(xAxis, amp, distance, sigma, num):
    # Initialize the function
    F_x = np.zeros_like(x)
    for i in range(-num, num + 1):
        F_x += amp * np.exp(-((xAxis - i * distance)**2) / (2 * sigma**2))
    return(F_x)

controlPlot = np.array(combGaussian(x, A, d, sigmaDiv, N))

testPlot = na.convolution_2d_changing_kernel(controlPlot, gaussianMatrix, x)
#testPlot2 = na.convolution_2d_changing_kernel(combGaussian(x, 20,0.5, 0.005, 200), ga.matrixGaussian, x)

mk2ConvolvePlot = na.convolution_1and2D(controlPlot, gaussianMatrix, x, dataP.gaussian, "same")


gs = GridSpec(2,2, figure = fig)
ax1 = fig.add_subplot(gs[0,0:])
ax2 = fig.add_subplot(gs[1,0])
ax3 = fig.add_subplot(gs[1,1])

ax1.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'lightblue', linewidth = 3)
ax1.plot(x, testPlot, label='Convolved Gaussian Comb', color = "indigo")


ax2.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'lightblue', linewidth = 3)
ax2.plot(x, testPlot, label='Convolved Gaussian Comb', color = "indigo")
#ax2.plot(x, mk2ConvolvePlot, label='New Convolution Func Comb', color = "red")


ax3.plot(x, mk2ConvolvePlot, label='New Convolution Func Comb', color = "red")

print(x)

fig.suptitle("GridSpec")

plt.show()