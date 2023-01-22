from matplotlib import pyplot
import warnings
from numpy import arange
import math
warnings.filterwarnings("ignore")  # To ignore a ComplexWarning later on, the warning doesnt effect the results.

# <-------------Decomposition of driven damped harmonic oscillator equation into two differential equations of first order --------------->

# x'' + w**2 x + gamma * x' - f_not * cos(w_not * t) = 0 , t = 0, x(0) = 1 , v(0) = 1
# x'' = - w**2 x - gamma * x' + f_not * cos(w_not * t)
# x ' = u  ------> f(t,x,x')
# u ' = - w **2 x - gamma * x' + f_not * cos(w_not * t) -------> f(t,x,u)

# initially f_not is 0 so ,
# u ' = - w**2 x - gamma * x'

# <--------------------------------------------------------------------------------------------------------------------------------------->

def f(t, x, u, gamma):  # code representation of -w**2 x - gamma * x
    return -81 * x - gamma * u  # remember that, w = 9 and x' = u


t = 0
x = 1
u = 1
tf = float(input("Enter the final time :"))
h = float(input("Enter step size:"))
gamma = float(input("Enter value of gamma:"))  # you can try different values of gamma
time_points = []
x_points = []
v_points = []
while t < tf:
    # Runge kutta 4 applied to decomposed first order differential equations
    m1 = u
    k1 = f(t, x, u, gamma)
    m2 = u + (h / 2) * k1
    t_2 = t + (h / 2)
    x_2 = x + (h / 2) * m1
    u_2 = m2
    k2 = f(t_2, x_2, u_2, gamma)
    m3 = u + (h / 2) * k2
    t_3 = t + (h / 2)
    x_3 = x + (h / 2) * m2
    u_3 = m3
    k3 = f(t_3, x_3, u_3, gamma)
    m4 = u + h * k3
    t_4 = t + h
    x_4 = x + h * m3
    u_4 = m4
    k4 = f(t_4, x_4, u_4, gamma)
    t = t + h
    x = x + (h / 6) * (m1 + (2 * m2) + (2 * m3) + m4)
    u = u + (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
    time_points.append(t)
    x_points.append(x)
    v_points.append(u)

pyplot.plot(time_points, x_points)
pyplot.plot(time_points, v_points)
pyplot.xlabel("time")
pyplot.ylabel("displacement/Amplitude and velocity ")
pyplot.legend(["displacement", "velocity"])
pyplot.show()


# wd(omega damped) = w * (1 - gamma ** 2 / 4 * w **2) ** 0.5 , notice that in wd , d is in the subscript of w
# T(omega) = 2* pi / wd
# w = 9

def T_as_function_of_gamma(gamma):
    a = gamma ** 2 / 324
    b = 1 - a
    wd = 9 * (b ** 0.5)
    T = 2 * 3.14 / wd
    return T


# T = 0.697 for gamma = 0.0
# T = 0.698 for gamma = 1.0
# T = 0.702 for gamma = 2.0
# .         .             .
# .         .             .
# .         .             .

# If the spring is not being able to complete its first oscillation , it means that time period is infinity
# for that wd(omega damped) should be equal to zero , so we need to find the value of gamma(critical gamma) for which wd is zero


def finding_critical_gamma():
    for i in range(0, 1000):  # trying to find the value of critical gamma in first 1000 numbers, can input any range of numbers
        a = i ** 2 / 324
        b = 1 - a
        wd = 9 * (b ** 0.5)
        if wd == 0:
            print("Omega critical = {}".format(i))
            break


gammas = arange(1.0, 18.0, 0.001)  # third argument in  arange function can be taken anything but it is taken as 0.001 for accuracy
# for gamma greater than 18.0, The Time period doesnt exist
T = []
for gamma in gammas:
    if gamma == 18.0:
        T.append(math.inf) # math.inf is a way to represent infinity 
    else:
        T.append(T_as_function_of_gamma(gamma))

pyplot.plot(gammas, T)
pyplot.xlabel("\u03B3")  # \u03B3  is a unicode character that represents symbol of gamma
pyplot.ylabel("T(\u03B3)")
pyplot.show()
# as seen in the plot , at gamma= 18, we get a vertical asymptote , because the Time period tends to infinity
