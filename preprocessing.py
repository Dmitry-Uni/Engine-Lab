import pandas as pd

df = pd.read_excel("Data/AAAAAA.xlsx", header=[0, 1])

def get_data(x_axis, y_axis):

    print("Preparing data...")
    df.replace(" -- ", 0, inplace=True)
    x_data = df[x_axis[0]][x_axis[1]]   
    y_data = df[y_axis[0]][y_axis[1]]

    x_units = x_data[0]
    y_units = y_data[0]
    print("Data prepared.")

    return [x_units, y_units], [x_data[2:], y_data[2:]]