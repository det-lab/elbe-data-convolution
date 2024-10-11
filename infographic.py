import numpy as np
import matplotlib.pyplot as plt

xAxis = np.array([1,2,3,4,5,6,7,8,9,10])

gaussian2D = ([4,2,0,0,0,0,0,0,0,0],
                      [4,4,2,0,0,0,0,0,0,0], 
                      [2,4,4,2,0,0,0,0,0,0],
                      [0,2,4,4,2,0,0,0,0,0],
                      [0,0,2,4,5,4,2,0,0,0],
                      [0,0,0,1,2,4,5,4,2,0],
                      [0,0,0,1,1,2,4,5,2,0],
                      [0,0,0,0,1,1,2,4,5,2],
                      [0,0,0,0,0,1,2,3,4,5],
                      [0,0,0,0,0,0,1,2,3,4],)

gaussian2D = np.array(gaussian2D)


signal = np.array([2,6,2,1,1,5,5,2,4,2])

def plotPoint(sig, gaussian2D):

    output = []

    for gaussian in gaussian2D:

        output.append(np.dot(sig, gaussian))

    return output

convolutionArray = plotPoint(signal, gaussian2D)

plt.plot(xAxis, signal, color = "blue")
plt.plot(xAxis, gaussian2D[0], color="red")
plt.plot(xAxis[0], convolutionArray[0], color="black", marker='o')

plt.ylim(0,65)

plt.show()