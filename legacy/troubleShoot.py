import numpy as np
import convolFunc

test1 = np.linspace(1,400,3000)
resTest = np.linspace(1000,2000,20)

padResTest = np.pad(resTest, 1490, mode = "constant", constant_values=0)

conv= np.convolve(test1,padResTest,mode="full")
funcCon = convolFunc.convolv(test1,padResTest)

print(resTest)

print(len(conv))
print(len(funcCon))