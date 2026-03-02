import roadster
import os
os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

#print(roadster.distance(0.5,"speed_elsa.npz"))
#print(roadster.reach(10000, 'speed_anna.npz'))
#print(roadster.reach(10000, 'speed_elsa.npz'))

import numpy as np
def format_hours_to_hms(hours):
    total_seconds = int(hours * 3600)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h}h {m}m {s}s"
import route_nyc
t0 = 4
h = 0.01
t_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
# first value in distance_km
print(f'Det tar {format_hours_to_hms(t_h[-1]-t_h[0])} timmar om man startar kl 4')
ref_value = 0
assert np.isclose(ref_value,distance_km[0]), 'first value in distance_km vector should be 0, since no distance has been traveled yet'

t0 = 9.5
h = 0.01

t_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
# first value in distance_km
print(f'Det tar {format_hours_to_hms(t_h[-1]-t_h[0])} timmar om man startar kl 9.30')