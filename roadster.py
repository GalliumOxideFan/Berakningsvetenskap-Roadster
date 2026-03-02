import numpy as np
from scipy import interpolate


def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    """
    Returns the estimated consumtion [Wh/km] at the given speed
    """
    a=[546.8, 50.31, 0.2584, 0.00821]
    v=abs(v)
    consumation = a[0]*v**-1+a[1]+a[2]*v+a[3]*v**2
    return consumation

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### Trapezoidal approximation
def trapezoid(fun, x_min, x_max, n):
    """
    Approximates an integral using trapezoidal approximation with arguments, input function, lower boundry, upper boundry, number of intervalls
    """
    points = np.linspace(x_min, x_max, n+1)
    h=(x_max-x_min)/(n)
    integral = h/2*(2*np.sum(fun(points))-fun(points[0])-fun(points[-1]))
    return integral
### PART 2A ###
def time_to_destination(x_target, route, n):
    """
    Estimates the time to reach x_target using trapezoidal approximation
    """
    def vel(x): return 1/velocity(x, route)
    time = trapezoid(vel, 0, x_target, n)
    return time

### PART 2B ###
def total_consumption(x_target, route, n):
    """
    Returns the total consumtion [Wh] from the start of the route to x_target km using trapezoidal approximation with n intervallt
    """
    def cons(x):
        return consumption(velocity(x, route))
    total_cons = trapezoid(cons, 0, x_target, n)
    return total_cons


def NR(f, f_prime, x0, tol):
    err = 2*tol
    x=x0
    while err > tol:
        fx, intErr = f(x)
        update = fx/f_prime(x)
        print(x)
        x = x - update
        err = np.abs(update)+np.abs(intErr)

    return x
### PART 3A ###
def distance(T, route):
    # The root of the non linear equation gives the driven distance
    tol = 10**-4
    x_guess = 0

    def ekv(x):
        n = 16
        err = tol*20
        while 100*np.abs(err)>tol: # Doubles n until good enouogh error to not effect NR SOLVER
            n*=2
            f = T - time_to_destination(x, route, n)
            err = (f-(T - time_to_destination(x, route, n//2)))/3 # Error approximation for trapezoidal method
        
        f = T - time_to_destination(x, route, n)
        err = (f-(T - time_to_destination(x, route, n//2)))/3 # Error approximation for trapezoidal method
        return f, err # passes err onto NR solver to allow for better handling of total error

    def ekv_prime(x): 
        return - 1/velocity(x,route)
    return NR(ekv, ekv_prime, x_guess, tol)

### PART 3B ###
def reach(C, route):

    tol = 10**-4
    distance_route = load_route(route)[0]
    x_guess = distance_route[-1] # We start at the end of the route and work backwards

    def ekv(x):
        n = 128
        err = tol*20
        while 100*np.abs(err)>tol: # Doubles n until good enouogh error to not effect NR SOLVER
            n*=2
            f = C - total_consumption(x, route, n)
            err = (f-(C - total_consumption(x, route, n//2)))/3 # Error approximation for trapezoidal method
        f = C - total_consumption(x, route, n)
        err = (f-(C - total_consumption(x, route, n//2)))/3 # Error approximation for trapezoidal method
        return f, err

    def ekv_prime(x): 
        return -consumption(velocity(x,route))
    
    if (ekv(x_guess)[0]/ekv_prime(x_guess))<=0: return x_guess # If it seems we have enough energy to reach the end, return the end value
    return NR(ekv, ekv_prime, x_guess, tol)
