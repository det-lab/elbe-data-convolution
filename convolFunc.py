import numpy as np
import matplotlib.pyplot as plt

#sameAxis = np.linspace(1,4,4)
#
#print(sameAxis)

list1 = np.linspace(5,250,2000)  # Test numbers before but now can be scaled [1,2,3,4,5]
list2 = np.linspace(0,300,2000)  # Test numbers before but now can be scaled [5,4,3,2,1]
list1 = np.pad(list1, len(list2)-1, mode= "constant", constant_values=0)

list1 = np.array(list1)
list2 = np.array(list2)


def convolv(list1, list2):
    #flip first array
    #list1Len = len(list1)
    #list2Len = len(list2)
    #if list2Len < list1Len:
    #    return print("List1 is greater than list2")
    
    rArray = []
    print(list1)
    for i in range(len(list1)):
        
        r = 0

        for j in range(len(list1)):
            
            if (i-j) < 0:
                break
            elif (j>= len(list2)) or ((i-j)>= len(list1)):
                break
            else:
                r += list2[j] * list1[i-j]


        rArray.append(r)
    
    return rArray

# keep np.dot in mind
                
        #n = 1
#
        #x = list2[n] * list1[n- i] + list2[1] * list1[n-i]
        #print(i)
        #print(list2[n], list1[n - i],  list2[1],  list1[n-i])
#
        #print(x)


x1_Value = np.linspace(-10,10,21) # n in y(n) convolve h(n)

def yFunc(m):
    yvalue = []
    for i in range(len(x1_Value)):
        if m[i] >= 0 and m[i] <2 or m[i] == 0 or  m[i] == 2:
            yvalue.append(m[i] * 2)
        else:
            yvalue.append(0)

    return yvalue
        
#h2_value = np.linspace(0,3,3)
def hFunc(m):
    hvalue = []
    for i in range(len(x1_Value)):
        if m[i] >= 0 and m[i] <2 or m[i] == 0 or  m[i] == 2:
            hvalue.append(1)
        else:
            hvalue.append(0)

    return hvalue

def sumation():

    newValueList = []

    for i in range(x1_Value):

        for j in range(len(x1_Value)):
            
            r = sum(hFunc(x1_Value[j]) * yFunc(x1_Value[i] - x1_Value[j]))
        
        print(i)
        print(sum(hFunc(m) * yFunc(i-m)))

    
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

print(len(cleanArry))

convovleTestArry = np.convolve(list1,list2,mode="same")
cleanConTestArry = cleanEdges(convovleTestArry)
print(len(cleanConTestArry))

for i in range(len(cleanArry)):
    if np.round(cleanArry[i],decimals=5) != np.round(cleanConTestArry[i],decimals=5):
        
        print("### cleanArry and cleanCOnTestArry are not equal at", i,"###")
    elif len(cleanArry) != len(cleanConTestArry):
        print("### Arrays are not the same dimentions ###")





#convolveFunc = np.convolve(yFunc(x1_Value),hFunc(x1_Value), mode="same")
#
#plt.plot(x1_Value, convolveFunc, color = "red")
#
#
#plt.plot(x1_Value,yFunc(x1_Value))
#plt.plot(x1_Value,hFunc(x1_Value))
#plt.show()

