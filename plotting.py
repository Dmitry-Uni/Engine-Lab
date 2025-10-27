import matplotlib.pyplot as plt
from preprocessing import get_data

class Plotter:

    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis


    def plot_data(self):

        print("Plotting data...")
        (x_units, y_units), (x_data, y_data) = get_data(self.x_axis, self.y_axis)
        print(f"x units: {x_units}, y units: {y_units}")

        plt.figure(figsize=(10, 6))
        plt.scatter(list(x_data), list(y_data), label=f"{self.y_axis[1]} vs {self.x_axis[1]}")
        plt.xlabel(f"{self.x_axis[1]} {x_units}")
        plt.ylabel(f"{self.y_axis[1]} {y_units}")
        plt.title(f"{self.y_axis[1]} vs {self.x_axis[1]}")
        plt.legend()
        plt.grid(True)
        print("Data plotted.")
        plt.show()