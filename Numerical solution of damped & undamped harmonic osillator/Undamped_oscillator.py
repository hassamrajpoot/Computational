from numpy import arange
from matplotlib import pyplot
m = float(input("Enter the value of mass here :"))
gamma = float(input("Enter the value of gamma :"))
x = float(input("Enter the value of x max:"))  # x max is the maximum amplitude
w = 9
k = m * w**2  # w = (k/m) **0.5
time_points = arange(0, 15, 0.1)  # always take a short interval and small step size
E_as_function_of_t = []
for t in time_points:
    E0 = 0.5 * k * x ** 2
    E = E0 / (2.718 ** (gamma * t))
    E_as_function_of_t.append(E)

pyplot.plot(time_points, E_as_function_of_t)
pyplot.xlabel("t")
pyplot.ylabel("E(t)")
pyplot.show()
# Notice that energy is decreasing constantly in an exponential manner , so the functional rule governing the decay is the exponential function
# because the energy decreases exponentially

