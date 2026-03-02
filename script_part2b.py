import roadster
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

route_anna_distance, route_anna_speed = roadster.load_route("speed_anna.npz")
route_elsa_distance, route_elsa_speed = roadster.load_route("speed_elsa.npz")

annaCons = roadster.total_consumption(route_anna_distance[-1], "speed_anna.npz", 2000)
elsaCons = roadster.total_consumption(route_elsa_distance[-1], "speed_elsa.npz", 2000)

print("Total energy consumption for Anna to arrive to destination", round(annaCons), "[Wh]")
print("Total energy consumption for Elsa to arrive to destination", round(elsaCons), "[Wh]")