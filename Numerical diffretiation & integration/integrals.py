import numpy
from matplotlib import pyplot
import math
# Exercises on integration
# Part one


def Trapezoidal_rule(f, a, b, n):
    del_x = (b - a) / n
    y0 = f(a)
    y_final = f(b)
    sum1 = (y0 / 2) + (y_final / 2)
    sum2 = 0
    for i in range(1, n+1):
        sum2 = sum2 + f(a + i * del_x)
    return del_x * (sum1 + sum2)


def Simpsons_rule(f, a, b, n):
    del_x = (b - a) / n
    final = []
    for i in range(a, n+1):
        if i != 1 and i != n+1:
            if i % 2 == 0:
                final.append(4 * f(a + i * del_x))
            else:
                final.append(2 * f(a + i * del_x))
        else:
            final.append(f(a + i * del_x))
    return round((del_x * (1 / 3)) * sum(final), 3)

# Part two
# using mid point approximation to find the integral of sin  from x = 0 to x =1 at different step sizes


def intMidPoint(f, a, b, n):
    h = (b - a) / n
    r = 0.0
    y = a + h*0.5
    for i in range(n):
        r = r + f(y)
        y = y + h
    r = r*h
    return [r, h]


def integrals_at_steps(no_of_intervals):
    integrals = []
    steps = []
    for n in no_of_intervals:
        integrals.append(intMidPoint(numpy.sin, 0, 1, n)[0])
        steps.append(intMidPoint(numpy.sin, 0, 1, n)[1])
    for i in range(0, len(integrals)):
        print("integral at step size = {} is {}".format(round(steps[i], 2), integrals[i]))
    return None

# Part three


def integrals_at_steps_new(no_of_intervals):
    integrals = []
    steps = []
    for n in no_of_intervals:
        integrals.append(intMidPoint(numpy.sin, 0, 1, n)[0])
        steps.append(intMidPoint(numpy.sin, 0, 1, n)[1])
    return [integrals, steps]


def comparison(no_of_intervals):
    x = integrals_at_steps_new(no_of_intervals)[1]
    y = integrals_at_steps_new(no_of_intervals)[0]
    x1 = math.dist([x[0], y[0]], [x[1], y[1]])
    x2 = math.dist([x[1], y[1]], [x[2], y[2]])
    pyplot.scatter(x, y)
    pyplot.xlabel("Step size")
    pyplot.ylabel("Integrals as function of step size")
    pyplot.annotate("p3", (x[0], y[0]))
    pyplot.annotate("p2", (x[1], y[1]))
    pyplot.annotate("p1", (x[2], y[2]))
    print("p3 - p2 = {}".format(round(x1, 3)))
    print("p2 - p1 = {}".format(round(x2, 3)))
    pyplot.show()


# p2 - p1 = 0.083  and p3 - p2 = 0.25 at step sizes [0.5, 0.25, 0.166]
# p2 - p1 = 0.017  and p3 - p2 = 0.025 at step sizes [0.125, 0.1, 0.083]
# which shows that as step sizes (h) decrease , the distance between points also decrease ( So the integrals converge)
