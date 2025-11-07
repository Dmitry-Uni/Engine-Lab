from preprocessing import get_data

# =============================================================================
    #Stroke plots
# =============================================================================

unit, RPM = get_data(("DTS2 Engine Torque & Speed", "Speed"), ("DTS2 Engine Torque & Speed", "Speed"))

minRPM = min(RPM[0][2:-2])
minRPMid = list(RPM[0]).index(minRPM)

maxRPM = max(RPM[0])
maxRPMid = list(RPM[0]).index(maxRPM)

