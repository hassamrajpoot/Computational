from matplotlib import pyplot
from numpy import cos
# almost the same thing as part one , just need to add a driving force

def f(t, x, u, gamma, f0, w0):
    return -81 * x - gamma * u + f0 * cos(w0 * t)  # w0 is the driving frequency , so any value can be taken as w0


t = 0
x = 1
u = 1
tf = float(input("Enter the final time :"))
h = float(input("Enter step size:"))
gamma = float(input("Enter value of gamma:"))
f0 = float(input("Enter value of f not :"))
w0 = float(input("Enter value of driving frequency :"))
time_points = []
x_points = []
v_points = []
while t < tf:
    m1 = u
    k1 = f(t, x, u, gamma, f0, w0)
    m2 = u + (h / 2) * k1
    t_2 = t + (h / 2)
    x_2 = x + (h / 2) * m1
    u_2 = m2
    k2 = f(t_2, x_2, u_2, gamma, f0, w0)
    m3 = u + (h / 2) * k2
    t_3 = t + (h / 2)
    x_3 = x + (h / 2) * m2
    u_3 = m3
    k3 = f(t_3, x_3, u_3, gamma, f0, w0)
    m4 = u + h * k3
    t_4 = t + h
    x_4 = x + h * m3
    u_4 = m4
    k4 = f(t_4, x_4, u_4, gamma, f0, w0)
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
