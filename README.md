# Tesla Roadster Range Estimation

**Project for Scientific Computing**
**Uppsala University**
**Course:** Numerical Methods / Scientific Computing

---

# Tesla Roadster Range Estimation Assignment

**Course:** Scientific Computing / Numerical Methods
**University:** Uppsala University

---

## Overview
This assignment focuses on **numerical methods** for estimating the range of an electric vehicle (Tesla Roadster) based on:
- Energy consumption as a function of speed.
- Speed data along a given route.

The project is divided into **four parts**:
1. **Data Handling**: Implement functions for energy consumption and speed interpolation.
2. **Numerical Integration**: Use the trapezoidal rule to estimate travel time and energy consumption.
3. **Root-Finding**: Apply Newton’s method to solve for distance and range.
4. **Differential Equations**: Simulate trips using Euler’s method.

The goal is to practice numerical techniques, including interpolation, integration, root-finding, and solving initial value problems.


---

## Repository Structure
```
roadster/
│
├── roadster.py          # Main implementation file
├── route_nyc.py         # NYC route simulation
├── speed_anna.npz       # Route data for Anna
├── speed_elsa.npz       # Route data for Elsa
├── test_roadster.py     # Test cases
├── script_part1a.py     # Script for Part 1(a)
├── script_part1b.py     # Script for Part 1(b)
├── script_part2a.py     # Script for Part 2(a)
├── script_part2b.py     # Script for Part 2(b)
├── script_part2c.py     # Script for Part 2(c)
├── script_part4a.py     # Script for Part 4(a)
├── script_part4b.py     # Script for Part 4(b)
└── README.md            # Project documentation

```

---

## Setup

### Prerequisites
- **Python 3.8+**
- Required libraries: `numpy`, `matplotlib`, `pytest`, `scipy`

Install dependencies:
```bash
pip install numpy matplotlib pytest scipy
```

### Clone the Repository
```bash
git clone https://github.com/GalliumOxideFan/Berakningsvetenskap-Roadster
cd roadster-range-estimation
```

## Project Parts

### **Part 1: Warm-up**
- **1(a):** Implement `consumption(v)` to calculate energy consumption (Wh/km) as a function of speed (km/h).
- **1(b):** Load and plot route data for Anna and Elsa. Use `velocity(x, route)` to interpolate speed data.

### **Part 2: Integration**
- **2(a):** Implement `time_to_destination(x, route, n)` to estimate travel time using the trapezoidal rule.
- **2(b):** Implement `total_consumption(x, route, n)` to estimate total energy consumption.
- **2(c):** Perform a convergence study for the trapezoidal rule.

### **Part 3: Root Finding**
- **3(a):** Implement `distance(T, route)` to estimate distance traveled in time `T` using Newton's method.
- **3(b):** Implement `reach(C, route)` to estimate range for a given battery charge `C`.

### **Part 4: Initial Value Problem**
- **4(a):** Implement `nyc_route_traveler_euler(t0, h)` to simulate a trip along a NYC route using Euler's method.
- **4(b):** Plot the trip data on the provided speed heatmap.

---

## How to Run

### Run Scripts
Execute the scripts for each part:
```bash
python script_part1a.py
python script_part1b.py
python script_part2a.py
python script_part2b.py
python script_part2c.py
python script_part3ab.py
python script_part4a.py
python script_part4b.py
```

### Run Tests
Use `pytest` to run the tests for each part:
```bash
pytest -k part1a    # Run tests for Part 1a
pytest -k part1    # Run tests for Part 1
pytest -k part2    # Run tests for Part 2
pytest             # Run all tests
```

Or from a Python prompt:
```python
import pytest
pytest.main(["-k", "part1"])  # Run tests for Part 1
```

---

## Key Functions

| Function                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `consumption(v)`              | Returns energy consumption (Wh/km) for a given speed `v` (km/h).           |
| `velocity(x, route)`          | Returns interpolated speed (km/h) at distance `x` (km) for a given route.  |
| `time_to_destination(x, route, n)` | Estimates travel time (h) for distance `x` (km) using the trapezoidal rule. |
| `total_consumption(x, route, n)` | Estimates total energy consumption (Wh) for distance `x` (km).           |
| `distance(T, route)`          | Estimates distance (km) traveled in time `T` (h) using Newton's method.    |
| `reach(C, route)`             | Estimates range (km) for a battery charge `C` (Wh).                        |
| `nyc_route_traveler_euler(t0, h)` | Simulates a trip starting at time `t0` (h) using Euler's method.       |

---

## Example Usage
```python
import roadster

# Calculate energy consumption at 90 km/h
print(roadster.consumption(90))

# Estimate travel time for Anna's route
time = roadster.time_to_destination(50, 'speed_anna', 1000)
print(f"Time to destination: {time} hours")

# Simulate a trip starting at 4:00 AM
time_h, distance_km, speed_kmph = roadster.nyc_route_traveler_euler(4.0, 0.1)
```

---

## Notes
- The trapezoidal rule is implemented from scratch.
- Newton-Raphson's method is used for root-finding in Parts 3(a) and 3(b).
- Euler's explicit method is used for simulating trips in Part 4.

---

## License
This project is licensed under **CC-BY-NC-SA-4.0**.
---

## Contributors
- [Gustav](https://github.com/GalliumOxideFan)
- Valdemar
- Uppsala University, Department of Information Technology
- MistralAI was used to write this description
