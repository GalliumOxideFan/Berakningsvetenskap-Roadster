#!/usr/bin/env python3
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1, 200, 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)
plt.rcParams.update({'font.size': 16})  # Set default font size for all text
plt.rcParams['lines.linewidth'] = 3
plt.plot(speed_kmph, consumption_Whpkm)
plt.xlabel("Speed [km/h]")
plt.ylabel("Consumption [Wh/km]")
plt.grid()
plt.show()