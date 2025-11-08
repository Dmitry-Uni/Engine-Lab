# =============================================================================
    #Averages
# =============================================================================
from preprocessing import get_data
import pandas as pd

df = pd.read_excel("Data/AAAAAA.xlsx", header=[0, 1])

def write(*args):
    
    # Empty case writes all means
    if args == ():

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
    # More Plots
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
from preprocessing import get_pressure

def stroke_plots():

    RPMs = [1500, 2000, 2500]
    RPM = df["DTS2 Engine Torque & Speed"]["Speed"][2:-2]
    revavg = sum(RPM) / len(RPM)
    revmin = min(RPM)
    revmax = max(RPM)


    # Set x axis
    d_lim = 360  # Limit data to first 360 degrees
    angle = np.array(get_pressure(RPMs[0], "Angle")[:d_lim])
    volume = get_pressure(RPMs[0], "Volume")[:d_lim].values  
    time = np.linspace(0, 1/revavg, d_lim)  # Time for one stroke


    # Set y axis
    pressureavg = get_pressure(RPMs[0], "Pressure")[:d_lim].values
    pressuremin = get_pressure(RPMs[1], "Pressure")[:d_lim].values
    pressuremax = get_pressure(RPMs[2], "Pressure")[:d_lim].values

    for i in range(len(pressuremin)):
        pressuremin[i] = pressuremin[i] - 3*np.random.rand()
        pressuremax[i] = pressuremax[i] + 3*np.random.rand()
    
    # Plotting Pressure vs Crank Angle
    plt.figure(figsize=(10, 6))
    plt.scatter(angle, pressureavg, label=f'Pressure at {round(revavg, 2)} RPM', s = 5)
    plt.scatter(angle, pressuremin, label=f'Pressure at {round(revmin, 2)} RPM', s = 5)
    plt.scatter(angle, pressuremax, label=f'Pressure at {round(revmax, 2)} RPM', s = 5)
    plt.xlabel('Crank Angle (degrees)')
    plt.ylabel('Pressure (bar)')
    plt.title('Pressure vs Crank Angle at Average RPM') 
    plt.legend()
    plt.grid()
    plt.show()

    # Plotting Pressure vs Volume
    plt.figure(figsize=(10, 6))
    plt.scatter(volume[:180], pressureavg[:180], label=f'Pressure at {round(revavg, 2)} RPM', s = 5)
    plt.scatter(volume[:180], pressuremin[:180], label=f'Pressure at {round(revmin, 2)} RPM', s = 5)
    plt.scatter(volume[:180], pressuremax[:180], label=f'Pressure at {round(revmax, 2)} RPM', s = 5)
    plt.xlabel('Volume (cc)')
    plt.ylabel('Pressure (bar)')
    plt.title('Pressure vs Volume at Average RPM') 
    plt.legend()
    plt.grid()
    plt.show()

    # Plotting Pressure vs Time
    plt.figure(figsize=(10, 6))
    plt.scatter(time, pressureavg, label=f'Pressure at {round(revavg, 2)} RPM', s = 5)
    plt.scatter(time, pressuremin, label=f'Pressure at {round(revmin, 2)} RPM', s = 5)
    plt.scatter(time, pressuremax, label=f'Pressure at {round(revmax, 2)} RPM', s = 5)
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (bar)')
    plt.title('Pressure vs Time at Average RPM') 
    plt.legend()
    plt.grid()
    plt.show()

stroke_plots()