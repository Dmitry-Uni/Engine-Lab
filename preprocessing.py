import pandas as pd


df = pd.read_excel("Data/AAAAAA.xlsx", header=[0, 1])


#print(df.columns)
#print(energy_data)
print(df["Calculated Parameters (Energy)"]["Heat Of Combustion"][0]) #Units