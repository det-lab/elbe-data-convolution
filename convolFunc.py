import numpy as np
import matplotlib.pyplot as plt
from numba import jit

preList1 = np.linspace(5,10,12)  # Test numbers before but now can be scaled [1,2,3,4,5]
preList2 = np.linspace(0,10,12)  # Test numbers before but now can be scaled [5,4,3,2,1]
list1 = np.pad(preList1, len(preList2)-1, mode= "constant", constant_values=0)


list1 = np.array(list1)
list2 = np.array(preList2)

@jit(nopython = True)
def convolv(list1, list2):
    
    rArray = []
    #Minus 1 in the inital value due to an even/odd relation for deviding the lengths by two 
    for i in range(int(len(list1)/2)-1 ,len(list1)- ((len(preList2)-1)/2)):
        
        r = 0

        for j in range(len(list1)):
            
            if (i-j) < 0:
                break
            elif (j>= len(list2)) or ((i-j)>= len(list1)):
                break
            elif (list2[j] != 0 and list1[i-j] != 0):
                r += list2[j] * list1[i-j]

        rArray.append(r)
    
    return rArray

# keep np.dot in mind

x1_Value = np.linspace(-10,10,21) # n in y(n) convolve h(n)

def cleanEdges(arry):

    startIdx = 0
    endIdx= len(arry)

    for i in range(len(arry)):
        if arry[i] != 0:
            startIdx= i
            
            break
    for i in range(len(arry) - 1, -1, -1):        
        if arry[i] !=0:
            endIdx = i
            break
    
    return arry[startIdx:endIdx]

rawArry = convolv(list1,list2)
cleanArry = cleanEdges(rawArry)

convovleTestArry = np.convolve(preList1,preList2,mode="same")
cleanConTestArry = cleanEdges(convovleTestArry)

print("Length of Convolution testing array", len(cleanConTestArry),"\n", "Length of data array", len(cleanArry))

print(cleanConTestArry,"\n", cleanArry)


for i in range(len(cleanArry)):
    if np.round(cleanArry[i],decimals=3) != np.round(cleanConTestArry[i],decimals=3):
        
        print("### cleanArry and cleanConTestArry are not equal at", i, "###")
        print("### cleanArry =", cleanArry[i], "cleanConTestArry =", cleanConTestArry[i], "###","\n")
        break
    elif len(cleanArry) != len(cleanConTestArry):
        print("### Arrays are not the same dimention ###")
        print(len(cleanConTestArry),"\n", len(cleanArry))
        break



#def yFunc(m):
#    yvalue = []
#    for i in range(len(x1_Value)):
#        if m[i] >= 0 and m[i] <2 or m[i] == 0 or  m[i] == 2:
#            yvalue.append(m[i] * 2)
#        else:
#            yvalue.append(0)
#
#    return yvalue
#        
##h2_value = np.linspace(0,3,3)
#def hFunc(m):
#    hvalue = []
#    for i in range(len(x1_Value)):
#        if m[i] >= 0 and m[i] <2 or m[i] == 0 or  m[i] == 2:
#            hvalue.append(1)
#        else:
#            hvalue.append(0)
#
#    return hvalue
#
#
#def sumation():
#
#    newValueList = []
#
#    for i in range(x1_Value):
#
#        for j in range(len(x1_Value)):
#            
#            r = sum(hFunc(x1_Value[j]) * yFunc(x1_Value[i] - x1_Value[j]))
#        
#        print(i)
#        print(sum(hFunc(m) * yFunc(i-m)))
#


#convolveFunc = np.convolve(yFunc(x1_Value),hFunc(x1_Value), mode="same")
#
#plt.plot(x1_Value, convolveFunc, color = "red")
#
#
#plt.plot(x1_Value,yFunc(x1_Value))
#plt.plot(x1_Value,hFunc(x1_Value))
#plt.show()

