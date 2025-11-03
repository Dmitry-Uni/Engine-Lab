import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
from preprocessing import get_data

class Plotter:
    def __init__(self, x_axis, y_axis, *additional_y_axes, secondary_threshold=5.0, two_sided_threshold=False):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.additional_y_axes = additional_y_axes
        self.secondary_threshold = float(secondary_threshold)
        self.two_sided_threshold = bool(two_sided_threshold)
        self._color_cycle = cycle(plt.cm.tab20.colors)

    @staticmethod
    def _to_numeric(series_like):
        if isinstance(series_like, pd.Series):
            return pd.to_numeric(series_like, errors='coerce')
        return pd.to_numeric(pd.Series(series_like), errors='coerce')
    
    def _next_color(self):
        return next(self._color_cycle)

    def plot_data(self):
        print("Plotting data...")

        result = get_data(self.x_axis, self.y_axis, *self.additional_y_axes)

        add_units, add_data = [], []
        (x_units, y_units), (x_data, y_data) = result[:2]
        if len(result) >= 4:
            add_units, add_data = result[2], result[3]

        x = self._to_numeric(x_data).reset_index(drop=True)
        y = self._to_numeric(y_data).reset_index(drop=True)

        n_main = min(len(x), len(y))
        x = x.iloc[:n_main]
        y = y.iloc[:n_main]

        extras = []
        for i, s in enumerate(add_data):
            name = self.additional_y_axes[i][1] if i < len(self.additional_y_axes) else f"Y{i+2}"
            unit = add_units[i] if i < len(add_units) else ""
            s_clean = self._to_numeric(s).reset_index(drop=True)
            n = min(len(x), len(s_clean))
            extras.append({"name": name, "unit": unit, "data": s_clean.iloc[:n]})

        # Classify ALL extras with the same rule
        primary_max = np.nanmax(y.values) if len(y) else np.nan
        primary_axis_extras = []
        secondary_axis_extras = []

        for e in extras:
            d = e["data"].values
            emax = np.nanmax(d) if d.size else np.nan

            # Default to primary if missing/invalid
            if np.isnan(primary_max) or np.isnan(emax) or primary_max == 0:
                primary_axis_extras.append(e)
                continue

            ratio = emax / primary_max

            if ratio >= self.secondary_threshold:
                secondary_axis_extras.append(e)
            elif self.two_sided_threshold and ratio <= (1.0 / self.secondary_threshold):
                secondary_axis_extras.append(e)
            else:
                primary_axis_extras.append(e)

        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Main
        print("x-axis:", self.x_axis[1])
        print("Core data:", self.y_axis[1])
        c_main = self._next_color()
        ax.scatter(x, y, color=c_main, label=f"{self.y_axis[1]} {y_units}")

        # PRIMARY-AXIS EXTRAS
        print("Primaries:", [e["name"] for e in primary_axis_extras])
        for e in primary_axis_extras:
            c = self._next_color()
            ax.scatter(x.iloc[:len(e['data'])], e["data"], color=c, marker='x',
                    label=f"{e['name']} {e['unit']} {'Primary data'}")

        ax.set_xlabel(f"{self.x_axis[1]} {x_units}")
        ax.set_ylabel(f"{self.y_axis[1]} {y_units}")

        # Secondary
        ax2 = None
        print("Secondaries:", [e["name"] for e in secondary_axis_extras])
        if len(secondary_axis_extras) > 0:
            ax2 = ax.twinx()
            sec_units = [e["unit"] for e in secondary_axis_extras]
            if len(set(sec_units)) == 1:
                sec_label = f"{' & '.join([e['name'] for e in secondary_axis_extras])} [{sec_units[0]}]"
            else:
                sec_label = "Additional metrics (secondary axis)"

            for e in secondary_axis_extras:
                c = self._next_color()
                ax2.scatter(x.iloc[:len(e['data'])], e["data"], color=c, marker='^',
                            label=f"{e['name']} {e['unit']} ({'secondary data'})")
            ax2.set_ylabel(sec_label)

            h1, l1 = ax.get_legend_handles_labels()
            h2, l2 = ax2.get_legend_handles_labels()
            ax.legend(h1 + h2, l1 + l2, loc="best")
        else:
            ax.legend(loc="best")

        title_bits = [self.y_axis[1]]
        if extras:
            title_bits += [e["name"] for e in extras]
        ax.set_title(f"{' + '.join(title_bits)} vs {self.x_axis[1]}")
        ax.grid(True)

        print("Data plotted.")
        plt.tight_layout()
        plt.show()