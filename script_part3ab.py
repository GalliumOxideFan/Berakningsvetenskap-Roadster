import roadster
import os
os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

print(f'Elsa kommer {round(roadster.distance(0.5,"speed_elsa.npz"),2)} km på 30 min')
print(f'Anna kommer {round(roadster.distance(0.5,"speed_anna.npz"),2)} km på 30 min')
print(f'Elsa kommer {round(roadster.reach(10000, 'speed_elsa.npz'),2)} på 10 kWh')
print(f'Anna kommer {round(roadster.reach(10000, 'speed_anna.npz'),2)} på 10 kWh')
