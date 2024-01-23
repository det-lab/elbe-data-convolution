# Define a step function and plot
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    if x < 0:
        return 0
    elif 0 <= x < 5:
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