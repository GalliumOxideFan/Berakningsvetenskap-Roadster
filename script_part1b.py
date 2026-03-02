import roadster
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

route_anna_distance, route_anna_speed = roadster.load_route("speed_anna.npz")
route_elsa_distance, route_elsa_speed = roadster.load_route("speed_elsa.npz")

plt.scatter(route_anna_distance, route_anna_speed, label = "Anna")
plt.scatter(route_elsa_distance, route_elsa_speed, label = "Elsa")
plt.xlabel("Distance [km]", fontsize=20)
plt.ylabel("Speed [km/h]", fontsize=20)
plt.grid()
plt.xticks(fontsize=14)  # Increase font size for x-axis tick labels
plt.yticks(fontsize=14)  # Increase font size for y-axis tick labels
plt.legend(fontsize=18)


x_elsa = np.linspace(0, route_elsa_distance[-1], 10000)
x_anna = np.linspace(0, route_anna_distance[-1], 10000)
anna_interpol = roadster.velocity(x_anna, "speed_anna.npz")
elsa_interpol = roadster.velocity(x_elsa, "speed_elsa.npz")
plt.plot(x_anna, anna_interpol, label = "Anna interpolated")
plt.plot(x_elsa, elsa_interpol, label = "Elsa interpolated")

plt.show()