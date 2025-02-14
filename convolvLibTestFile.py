import numpy as np
import convolvLib as cl
import dataPull
import primaryConvolve as pc
import matplotlib.pyplot as plt
import random

axis = dataPull.neutronEnergyList
dataSet = dataPull.theoryValuesList

currentCon = pc.convolution_2d_changing_kernel(dataSet, dataPull.matrixGaussianFunc(axis), axis)

libraryConv = cl.convolve2D(cl.kernel, dataSet, axis)

if (currentCon==libraryConv).all():
    print("Same convolutions")
else:
    print("Diffrence found")

#analitical test case

#numpy convolution function

#numpyConvolv = np.convolve(dataSet, dataPull.matrixGaussianFunc(axis), mode="same")

#if (currentCon==numpyConvolv).all() and (libraryConv==numpyConvolv).all():
#    print("Same convolutions to numpy's convolution")
#else:
#    print("Diffrence found")

numpyConvolution = np.convolve(dataSet, dataPull.matrixGaussianFunc(axis)[0], mode="full")

singleDimConv = pc.convolution_1d_same(dataSet, dataPull.matrixGaussianFunc(axis)[0], axis)
"""
if (singleDimConv==numpyConvolution).all():
    print("Same convolutions to numpy's convolution")
else:
    print("Diffrence found")

#
"""


def convolutionTest1(convolutionFunc):
    axis = np.linspace(-10,10,200)

    arbitarySigma = 2

    trueAnalitical = 1/(np.sqrt(2*np.pi* (arbitarySigma**2 + arbitarySigma**2))) * np.exp(-(axis**2)/(2*(arbitarySigma**2 + arbitarySigma**2)))

    fFunction = (1/np.sqrt(2*np.pi*arbitarySigma**2)) * np.exp((-1 * axis**2)/(2*arbitarySigma**2))

    gFunction = fFunction

    return trueAnalitical, convolutionFunc(fFunction, gFunction, axis), fFunction, gFunction, axis
    
def convolutionTest2(convolutionFunc):
    axis = np.linspace(-10,10, 200)

    def TriangleFunc(arr):
        return np.where((arr >= 0) & (arr <= 2), arr, 0)
    
    def squareFunc(arr):
        return np.where((arr >= -2) & (arr <= 0), 5, 0)

    #introduce analitical solution from notes

    def analyilticlSolution(axis):
        output = np.zeros(len(axis))

        for i, x in enumerate(axis):
            if x < 0:
                output[i] = 0
            elif x >= 0 and x < 2:
                output[i] = (5/2)* (x**2)
            elif x == 2:
                output[i] = 10
            elif x > 2 and x < 4:
                output[i] = (10 * x -10) - (5*x*(x-2)-(5/2)*(x-2)**2)
            elif x >= 4:
                output[i] = 0
            else:
                print("Something broke")
        return output

    return analyilticlSolution(axis), convolutionFunc(TriangleFunc(axis), squareFunc(axis), axis), TriangleFunc(axis), squareFunc(axis), axis

def convolutionTest3(convolutionFunc):
    
    #make the axis non uniform stepping size
    def changeingStep():
        xAxis = np.linspace(-10,10,100)
        finalX = []
        for i, x in enumerate(xAxis):
            finalX.append(x * i)
        return finalX

    axis = changeingStep()

    axis = np.array(axis)
    print(np.diff(axis))
    arbitarySigma = 2

    trueAnalitical = 1/(np.sqrt(2*np.pi* (arbitarySigma**2 + arbitarySigma**2))) * np.exp(-(axis**2)/(2*(arbitarySigma**2 + arbitarySigma**2)))

    fFunction = (1/np.sqrt(2*np.pi*arbitarySigma**2)) * np.exp((-1 * axis**2)/(2*arbitarySigma**2))

    gFunction = fFunction

    return trueAnalitical, convolutionFunc(fFunction, gFunction, axis), fFunction, gFunction, axis

def plotConvolutionTest(testFunc, convolutionFunc):
    
    trueCon, testCon, kernal, signal, axis = testFunc(convolutionFunc)
    print(np.dot(kernal, signal) * np.diff(axis)[0])
    plt.plot(axis, trueCon, label= "True Con", color = "blue", )
    plt.plot(axis, testCon, label= "Test Con", color = "red")
    #plt.plot(axis, kernal, label= "Kernel Func", color = "yellow")
    #plt.plot(axis, signal, label= "Signal Func", color = "purple")
    #plt.plot(axis, np.convolve(kernal, signal, mode= "same") * np.diff(axis)[0])

    plt.legend(loc="upper left", fontsize = 24)

    plt.show()
    
plotConvolutionTest(convolutionTest2, pc.convolution_1and2D)



"""

def peiceWiseConvolve(kernelArray, dataSet, axis):

    kernelArrayLength = len(kernelArray)
    dataSetLength = len(dataSet)

    #create if statments for cases of unequal length arrays
    #needs to be able to check for aprox 5 total cases exluding edge cases such as trivial products

    if kernelArrayLength <= dataSetLength:
        leftSideIntergral()
        rightSideIntergral()
        if kernelArrayLength == dataSetLength:
            equalArrayIntergral()
        else:
            smallerKernalIntergral()
    elif kernelArrayLength >= dataSetLength:
        leftSideIntergral()
        rightSideIntergral()
        kernalOverlapIntergral()
"""