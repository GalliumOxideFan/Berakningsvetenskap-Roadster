import roadster
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

route_anna_distance, route_anna_speed = roadster.load_route("speed_anna.npz")
route_elsa_distance, route_elsa_speed = roadster.load_route("speed_elsa.npz")

annaTime = roadster.time_to_destination(route_anna_distance[-1], "speed_anna.npz", 300000)
elsaTime = roadster.time_to_destination(route_elsa_distance[-1], "speed_elsa.npz", 300000)

def format_hours_to_hms(hours):
    total_seconds = int(hours * 3600)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h}h {m}m {s}s"

annaTime = format_hours_to_hms(annaTime)
elsaTime = format_hours_to_hms(elsaTime)

print("Time for Anna to arrive to destination", annaTime)
print("Time for Elsa to arrive to destination", elsaTime)