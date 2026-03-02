import roadster
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import os

os.chdir(os.path.dirname(__file__)) #changes the working directory to folder that this file is in

absolute_truth = roadster.total_consumption(50, "speed_anna.npz", 10000000)
n_init = 10

c_max = 20 # Don't assign value higher than 20, programme dislikes it :(
n_list = np.zeros(c_max)
tot_cons_list = np.zeros(c_max)
error_list=np.zeros(c_max)

for i in range(0,c_max):
    n = n_init*2**i
    n_list[i] = n
    cons = roadster.total_consumption(50, "speed_anna.npz", n)
    tot_cons_list[i] = cons
    error = np.abs(cons-absolute_truth)
    error_list[i]=error

plt.rcParams.update({'font.size': 19})  # Set default font size for all text
plt.rcParams['lines.linewidth'] = 3
plt.loglog(n_list, error_list, label="Actual error")
plt.loglog(n_list, 100000/(n_list**2), label="1/n²")
plt.loglog(n_list, 100000/(n_list), label="1/n")
plt.loglog(n_list, 100000/(n_list**3), label="1/n³")
plt.xlabel("n", fontsize=25)
plt.ylabel("Error", fontsize = 25)
plt.legend()
plt.show()