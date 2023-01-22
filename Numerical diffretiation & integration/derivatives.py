from numpy import tan, sin
from matplotlib import pyplot
import math


# Exercises on derivation
# part one


def derBackwards(f, x, h):
    r = (f(x) - f(x - h)) / h
    return r


def derCentral(f, x, h):
    forward = f(x + h)
    backward = - f(x - h)
    return (forward + backward) / 2 * h


# part two

def derivative_at_steps(steps):
    # taking the derivatives of sin function at point 0.5
    derivatives = []
    for h in steps:
        r = (sin(0.5 + h) - sin(0.5)) / h
        derivatives.append(r)
    for i in range(0, len(derivatives)):
        print("derivative of sin at x=0.5 and step = {} is : {}".format(steps[i], derivatives[i]))
    return None


# part three


def derivatives_as_function_of_steps():
    steps = [0.1, 0.01, 0.001]
    derivatives = []
    for h in steps:
        r = (tan(0.5 + h) - tan(0.5)) / h
        derivatives.append(r)
    distances = [math.dist([steps[0], derivatives[0]], [steps[1], derivatives[1]]),
                 math.dist([steps[1], derivatives[1]], [steps[2], derivatives[2]])]
    pyplot.scatter(steps, derivatives)
    s1 = steps[0] - 0.01
    s2 = derivatives[0] - 0.01
    s3 = steps[1] + 0.002
    s4 = derivatives[1] - 0.005
    pyplot.xlabel("steps size")
    pyplot.annotate("p3", (steps[0] - 0.005, derivatives[0]))
    pyplot.annotate("p2", (steps[1] - 0.005, derivatives[1] + 0.001))
    pyplot.annotate("p1", (steps[2] - 0.004, derivatives[2] + 0.002))
    pyplot.ylabel("derivative as function of step size")
    pyplot.text(s1, s2, "p3 - p2 = {}".format(round(distances[0], 5)))
    pyplot.text(s3, s4, "p2 - p1 = {}".format(round(distances[1], 5)))
    pyplot.show()
    # if we keep on decreasing the step size (h) the distance between individual points also decreases , which means 
    # that the points converge.
