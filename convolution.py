# Define a step function and plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 

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



gaussianFunc = np.exp(-(x_values - mean)**2 / (2 * standDiv**2)) / (standDiv * np.sqrt(2 * np.pi))

plt.plot(x_values, gaussianFunc, 'k', linewidth=2)
plt.show()




# Convolve the Step function and the Gaussian Function and plot the convolved function

convolveFunc = np.convolve(gaussianFunc, y_value, mode='same')

plt.figure(figsize=(10,10))



plt.plot()
plt.plot(x_values, convolveFunc, linewidth = 2)
plt.title('Convolution Result')

plt.show()

#import energy data of CM frame to calculate energy in lab frame

cmFrameEnergy = pd.read_excel("data\FourteenN_n_excitation_function.xlsx",usecols="B", skiprows=lambda x: x in [0, 2])

#converts the dataFrame to a list for ease of use
cmFrameEngList = cmFrameEnergy["Unnamed: 1"].tolist()

#define the cm Energy to lab energy function
def convCmToLab(cmE):
    massT = 14.003074
    massP = 1.008665
    massRatio = (massP + massT)/(massT)
    return massRatio * cmE

#new list for the new values of energy in the lab frame
labFrame = [convCmToLab(result) for result in cmFrameEngList]

print("Coputation for lab frame is complete")

if os.path.exists("data\LabFrameEnergyData.xlsx"):
    print("A lab Frame excel sheet already exists")
else:
    labDataFrame = pd.DataFrame({"Lab Frame Energy": labFrame})

    labDataFrame.to_excel("LabFrameEnergyData.xlsx", index=False)

    #file destination manipulation after creation to keep data organized
    file_path = 'LabFrameEnergyData.xlsx'
    destination_directory = 'data/'

    new_file_path = os.path.join(destination_directory, os.path.basename(file_path))

    os.rename(file_path, new_file_path)

    print("File has been created and moved to", destination_directory)



### Code below is an inprogress for exporting the lab energy back into the same excel sheet of our data
#############################################################
#from openpyxl import load_workbook
#
#dataFileBook = load_workbook("data\FourteenN_n_excitation_function.xlsx")
#
#dataFile = dataFileBook.active
#
#columnIndex = 6
#
#startingRow = dataFile.max_row + 2
#
#for value in labFrame:
#    dataFile.cell(row=startingRow, column= columnIndex, value=value)
#    startingRow += 1
#
#dataFileBook.save("data\FourteenN_n_excitation_function.xlsx")
#############################################################
    