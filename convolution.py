# Define a step function and plot
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    if -6<= x < 6:
        return 1
    else:
        return 0
    
vectoredFunction = np.vectorize(step_function)

x_values = np.linspace(-10, 10, 1000)
y_value = vectoredFunction(x_values)

plt.plot(x_values, y_value, label="Step Function")
plt.grid(True)
plt.show()


# Define a gaussion function and plot

mean = 0
standDiv = 1

points = np.random.normal(mean, standDiv, 1000)
xmin = min(points)
xmax = max(points)

plt.hist(points, bins=50, density=True, alpha=0.6, color='g')

x = np.linspace(xmin, xmax, 100)

gaussianFunc = np.exp(-(x - mean)**2 / (2 * standDiv**2)) / (standDiv * np.sqrt(2 * np.pi))

plt.plot(x, gaussianFunc, 'k', linewidth=2)
plt.show()
print(xmin, xmax)



# Convolve the Step function and the Gaussian Function and plot the convolved function

convolveFunc = np.convolve(gaussianFunc, y_value, mode='full')

plt.figure(figsize=(10,10))

plt.plot()
plt.stem(convolveFunc)
plt.title('Convolution Result')

plt.show()