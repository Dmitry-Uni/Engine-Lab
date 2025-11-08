# =============================================================================
    #Averages
# =============================================================================
from preprocessing import get_data
import pandas as pd

def write(*args):
    
    # Empty case writes all means
    if args == ():

        df = pd.read_excel("Data/AAAAAA.xlsx", header=[0, 1])

        file_name = "Means.txt"
        with open(file_name, 'w') as file:
            file.write("Mean (Whole Dataset)\n")

            for col in df.columns:
                nzero_data = [item for item in get_data(col, col)[1][1:][0] if item != 0]
                if len(nzero_data) > 0:
                    file.write(f"{col[1]} Mean: {sum(nzero_data) / len(nzero_data)} \n")
                else:
                    file.write(f"{col[1]} Mean: No non-zero data available\n")

        return
    
    # Selected columns case, takes in args
    else: 
        file_name = "Means_Selected.txt"
        with open(file_name, 'w') as file:
            file.write("Mean (Selected Columns)\n")

            for col in args:
                nzero_data = [item for item in get_data(col, col)[1][1:][0] if item != 0]
                if len(nzero_data) > 0:
                    file.write(f"{col[1]} Mean: {sum(nzero_data) / len(nzero_data)} \n")
                    print(f"{col[1]} Mean: {sum(nzero_data) / len(nzero_data)} \n")
                else:
                    file.write(f"{col[1]} Mean: No non-zero data available\n")
                    print(f"{col[1]} Mean: No non-zero data available\n")
        return
    
# =============================================================================
    #Stroke plots
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
from preprocessing import get_pressure

def stroke_plots():

    RPMs = [1500, 2000, 2500]

stroke_plots()

# =============================================================================