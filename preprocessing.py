import pandas as pd

df = pd.read_excel("Data/AAAAAA.xlsx", header=[0, 1])

def get_data(x_axis, y_axis, *args):
    print("Preparing data...")

    df.replace(" -- ", 0, inplace=True)

    x_data = df[x_axis[0]][x_axis[1]]
    y_data = df[y_axis[0]][y_axis[1]]

    x_units = x_data.iloc[0]
    y_units = y_data.iloc[0]

    add_y_data = []
    add_y_units = []

    if args:
        for arg in args:
            s = df[arg[0]][arg[1]]
            add_y_units.append(s.iloc[0])
            add_y_data.append(s.iloc[2:])  # match slicing behaviour

    print("Data prepared.")

    if args:
        return [x_units, y_units], [x_data.iloc[2:-3], y_data.iloc[2:-3]], add_y_units, add_y_data
    else:
        return [x_units, y_units], [x_data.iloc[2:-3], y_data.iloc[2:-3]]