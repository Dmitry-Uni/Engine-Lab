from plotting import Plotter

    # =============================================================================
    # Excel Column Structure (first two header rows)
    #
    # Time
    #
    # AVF1, DVF1 Fuel Consumption
    #     - Fuel Consumption (mL.min⁻¹)
    #     - Fuel Consumption (kg.s⁻¹)
    #     - Fuel Density (kg.m⁻³)
    #     - Fuel Calorific Value (MJ.kg⁻¹)
    #
    # Calculated Parameters (Energy)
    #     - Heat Of Combustion (W)
    #     - Exhaust Gas Enthalpy (W)
    #     - Inlet Air Enthalpy (W)
    #     - Heat Loss To Exhaust (W)
    #
    # DPT1 Engine Air & Exhaust
    #     - Ambient Air Temperature (°C)
    #     - Exhaust Gas Temperature (°C)
    #     - Airbox Differential Pressure (Pa)
    #     - Ambient Air Pressure (Pa)
    #     - Orifice Diameter (m)
    #     - Air Mass Flow Rate (kg.s⁻¹)
    #
    # DTS2 Engine Torque & Speed
    #     - Torque (N·m)
    #     - Speed (rev.min⁻¹)
    #     - Power (W)
    #
    # TDX00A Exhaust Calorimeter
    #     - Water Inlet Temperature T1 (°C)
    #     - Water Outlet Temperature T2 (°C)
    #     - Exhaust Inlet Temperature T3 (°C)
    #     - Exhaust Outlet Temperature T4 (°C)
    #     - Cooling Water Flow Rate (L.min⁻¹)
    #
    # Calculated Parameters (Engine)
    #     - Air Fuel Ratio
    #     - Specific Consumption
    #     - Thermal Efficiency
    #     - Volumetric Efficiency
    #     - Engine Capacity (m³)
    #     - Number Of Cycles [2 or 4]
    #     - BMEP (bar)
    # =============================================================================

    # Example usage:
    # x_axis = ["Time", "Time"]
    # y_axis = ["Calculated Parameters (Energy)", "Heat Of Combustion"]
    # inlet_enthalpy_over_time = Plotter(x_axis, y_axis)
    #inlet_enthalpy_over_time.plot_data()

x_axis = ["Time", "Time"]
y_axis = ["Calculated Parameters (Energy)", "Heat Of Combustion"]
inlet_enthalpy_over_time = Plotter(x_axis, y_axis)
inlet_enthalpy_over_time.plot_data()

x_axis = ["Time", "Time"]
y_axis = ["Calculated Parameters (Energy)", "Inlet Air Enthalpy"]
inlet_enthalpy_over_time = Plotter(x_axis, y_axis)
inlet_enthalpy_over_time.plot_data()