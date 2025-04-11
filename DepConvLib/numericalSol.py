import numpy as np

tauLowerLim = -200
tauUpperLim = 200
xLowerLim = -200
xUpperLim = 200

def innerConvolvFunc(tau,xVal):
    return np.exp((-1 * tau**2)/(2*3**2)) * np.exp((-1 * (xVal-tau)**2)/(2*((tau+20)/5)**2))


def double_integral(f, ax, bx, ay, by, nx=100, ny=100):
    """
    Approximate the double integral of f(x, tau) over the rectangle [ax,bx] x [ay,by].

    Parameters:
        f:   function of two variables f(x, y)
        ax:  lower bound in x
        bx:  upper bound in x
        ay:  lower bound in y
        by:  upper bound in y
        nx:  number of subdivisions in x
        ny:  number of subdivisions in y

    Returns:
        Approximate value of the double integral
    """
    hx = (bx - ax) / nx
    hy = (by - ay) / ny

    x = np.linspace(ax, bx, nx + 1)
    y = np.linspace(ay, by, ny + 1)

    total = 0
    for i in range(nx + 1):
        for j in range(ny + 1):
            weight = 1
            if i == 0 or i == nx:
                weight *= 0.5
            if j == 0 or j == ny:
                weight *= 0.5
            total += weight * f(x[i], y[j])

    return hx * hy * total

areaUnderCruve = double_integral(innerConvolvFunc,xLowerLim,xUpperLim,tauLowerLim,tauUpperLim)

import matplotlib.pyplot as plt

# Define the function of two variables


# Create meshgrid for surface plot
x = np.linspace(-20, 20, 100)
tau = np.linspace(-20, 20, 100)
X, TAU = np.meshgrid(x, tau)
Z = innerConvolvFunc(X, TAU)

# Plot the surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, TAU, Z, cmap='viridis', edgecolor='none', alpha=0.8)
ax.set_title('Surface plot of f(x, tau)')
ax.set_xlabel('x')
ax.set_ylabel('tau')
ax.set_zlabel('f(tau, x)')

ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

print(areaUnderCruve)

plt.show()