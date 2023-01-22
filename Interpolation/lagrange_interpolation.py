import sympy
# interpolation and lagrange polynomials
# part one


def lagrange_interpolation(x_data, y_data, point):
    y = 0
    for i in range(len(x_data)-1):
        p = 1
        for j in range(len(x_data)-1):
            if i != j:
                p = p * (point - x_data[j]) / (x_data[i] - x_data[j])
        y = y + p * y_data[i]
    if y.is_integer():
        return int(y)
    else:
        return round(y, 3)

# Part Two
# choosing a  sine function over  interval  [0 , pi/2] and taking data points [0, 0.523, 1.04, 1.57] [0, 0.009, 0.018, 0.027]
# Remember to choose data points in radians , not in degrees


def interpolating_polynomial(x_data, y_data):
    y = 0
    x = sympy.Symbol("x")
    for i in range(len(x_data)):
        p = 1
        for j in range(len(x_data)):
            if i != j:
                p = p * (x - x_data[j]) / (x_data[i] - x_data[j])
        y = y + p * y_data[i]
    return sympy.simplify(y)

# The interpolated polynomial would be : x*(-0.000382072352341986*x**2 + 0.000789208691701321*x + 0.016900164724616)


# Part three


# Using 2 , 3, 5 data points and sin function
# The more number of data points we use , the close the approximated lagrange polynomial gets to the original sine function
# in an interval


def comparison(x_data_points, y_data_points):
    x = sympy.Symbol("x")
    expression = interpolating_polynomial(x_data_points, y_data_points)
    p1 = sympy.plotting.plot(expression, line_color="r", show=False)
    p2 = sympy.plotting.plot((sympy.sin(x), (x, -sympy.pi, sympy.pi)), show=False)
    p1.append(p2[0])
    p1.legend = True
    p1.show()


