import pandas as pd
import os

#import energy data of CM frame to calculate energy in lab frame

#cmFrameEnergy = pd.read_excel("data\FourteenN_n_excitation_function.xlsx",usecols="B", skiprows=lambda x: x in [0, 2])

# Define path components

folder = 'data'

filename = '14N_n_excitation_Function.xlsx'

# Build the path

file_path = os.path.join(folder, filename)

# Print the path

print(file_path)


totalExcelData = pd.read_excel(file_path, header=2, usecols="B:E")
print(totalExcelData.columns)
#converts the dataFrame to a list for ease of use
#cmFrameEngList = cmFrameEnergy["Unnamed: 1"].tolist()

#define the cm Energy to lab energy function
def convCmToLab(cmE):
    massT = 14.003074
    massP = 1.008665
    massRatio = (massP + massT)/(massT)
    return massRatio * cmE

#new list for the new values of energy in the lab frame
#labFrame = [convCmToLab(result) for result in cmFrameEngList]

totalExcelData["Lab Frame Energy"] = totalExcelData["Center of Mass Energy (MeV)"].apply(convCmToLab)

print("Coputation for lab frame is complete")



if os.path.exists("data\LabFrameEnergyData.xlsx"):
    print("A lab Frame excel sheet already exists")
else:
    #labDataFrame = pd.DataFrame({"Lab Frame Energy": labFrame})
    totalExcelData.to_excel("LabFrameEnergyData.xlsx", index=False)
    #labDataFrame.to_excel("LabFrameEnergyData.xlsx", index=False)

    #file destination manipulation after creation to keep data organized
    file_path = 'LabFrameEnergyData.xlsx'
    destination_directory = 'data/'

    new_file_path = os.path.join(destination_directory, os.path.basename(file_path))

    os.rename(file_path, new_file_path)

    print("File has been created and moved to", destination_directory)

#add data from origial data from excel 