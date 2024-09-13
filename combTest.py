import numpy as np
import newApproach as na
import gaussianAnim as ga
import matplotlib.pyplot as plt

x = ga.uniformNeutronEnergyList

# Parameters for the Gaussian comb
A = 20        # Amplitude
d = 1      # Distance between peaks
sigmaDiv = 0.1 # Standard deviation (width) of each Gaussian
N = 2000       # Number of terms in the summation on each side of the center



# Sum over the Gaussian functions
def combGaussian(xAxis, amp, distance, sigma, num):
    # Initialize the function
    F_x = np.zeros_like(x)
    for i in range(-num, num + 1):
        F_x += amp * np.exp(-((xAxis - i * distance)**2) / (2 * sigma**2))
    return(F_x)

controlPlot = np.array(combGaussian(x, 20, 0.5, 0.1, 200))

testPlot = na.convolution_2d_changing_kernel(controlPlot, ga.matrixGaussian, x)



# Plotting the result
plt.figure(figsize=(10, 6))
plt.plot(x, controlPlot, label='Repeating Gaussian Comb', color = 'blue')
plt.plot(x, testPlot, label='Convolved Gaussian Comb', color = "black")
plt.title('Repeating Gaussian Comb')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.legend()
plt.show()