import pandas as pd
import matplotlib.pyplot as plt
import cmEnergyConversion as cmConvert

azureAA2R1 = pd.read_csv("AZURE2-Output\AZUREOut_aa=2_R=1.extrap", sep='\s+', header=None)
azureAA2R2 = pd.read_csv("AZURE2-Output\AZUREOut_aa=2_R=2.extrap", sep='\s+', header=None)
azureAA2R3 = pd.read_csv("AZURE2-Output\AZUREOut_aa=2_R=3.extrap", sep='\s+', header=None)

azureCmEnergy = azureAA2R1[0]

azureCrossSec = [azureAA2R1[3], azureAA2R2[3], azureAA2R3[3], azureAA2R1[3]+ azureAA2R2[3] + azureAA2R3[3]] 

azureLabEnergy= []
for energy in azureCmEnergy:
    azureLabEnergy.append(cmConvert.convCmToLab(energy))

def cmFrameAzure():
    for i, (energy, crossSec) in enumerate(zip(azureCmEnergy, azureCrossSec)):
        plt.plot(energy, crossSec, label = f"AzureOut_aa=2_R{i+1}")
        plt.legend(loc="upper left")
        plt.xlabel("Center of Mass Energy (MeV)")
        plt.ylabel("Barns")

def labFrameAzure():

    
    #for i, (energy, crossSec) in enumerate(zip(azureLabEnergy, azureCrossSec)):
    plt.plot(azureLabEnergy, azureCrossSec[3], label = f"AzureOut_aa=2_R")
    plt.legend(loc="upper left")
    plt.xlabel("Lab Frame Energy (MeV)")
    plt.ylabel("Barns")
    

plt.show()