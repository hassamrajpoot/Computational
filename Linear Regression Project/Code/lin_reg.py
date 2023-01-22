import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


# function name: least_sq
# inputs: file_name- name of the csv file 
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
# LITERALLY return m, b (both rounded 4 decimal places)
# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y


def least_sq(file_name):
    df = pd.read_csv(file_name)
    x_values = df['x'].tolist()
    y_values = df['y'].tolist()
    N = len(x_values)
    sum_of_x_values = sum(x_values)
    sum_of_y_values = sum(y_values)
    sum_of_xy_values = sum([x * y for x, y in zip(x_values, y_values)])
    sum_of_x_squared_values = sum([x * x for x in x_values])
    m = (N * sum_of_xy_values - sum_of_x_values * sum_of_y_values) / (
            N * sum_of_x_squared_values - sum_of_x_values ** 2)
    b = (sum_of_y_values - m * sum_of_x_values) / N
    return round(m, 4), round(b, 4)


# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
# LITERALLY return m, b (both rounded 4 decimal places)
# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y


def mat_least_sq(file_name):
    df = pd.read_csv(file_name)
    x_values = df['x'].tolist()
    y_values = df['y'].tolist()
    y_values = np.asarray(y_values)
    x_values = [[value, 1] for value in x_values]
    X = np.asarray(x_values)
    X_transpose = X.transpose()
    X_transpose_X = np.dot(X_transpose, X)
    X_transpose_X_inverse = np.linalg.inv(X_transpose_X)
    X_transpose_y = np.dot(X_transpose, y_values)
    m = np.dot(X_transpose_X_inverse, X_transpose_y)[0]
    b = np.dot(X_transpose_X_inverse, X_transpose_y)[1]
    return round(m, 4), round(b, 4)


# function name: predict
# inputs: file_name- name of the csv file 
# x- input value that you will interpolate or extrapolate using mat_least_sq
# output: the predicted value based on the linear regression equation found using mat_least_sq
# The output should be rounded to 4 decimal places
# assumptions: The csv file will always have headers in the order of: x, y
def predict(file_name, x):
    m, b = mat_least_sq(file_name=file_name)
    y = m * x + b
    return round(y, 4)


# function name: plot_reg
# inputs: file_name- name of the csv file
# using_matrix: True if you are plotting the linear equation from mat_least_sq
# 				False if you are plotting the linear equation from least_sq
# output: nothing is returned
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
# your graph should have the following: labeled x and y axes, title, legend
# if using_matrix is False (using least_sq), use X's and red in your graph
# if using_matrix is True (using mat_least_sq), you can use any color except for the default blue and red
# you can use any marker except for the default dot and X
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
    if not using_matrix:
        df = pd.read_csv(file_name)
        x_values = df['x'].tolist()
        y_values = df['y'].tolist()
        slope, intercept = least_sq(file_name=file_name)
        y = [slope * x_val + intercept for x_val in x_values]
        plt.scatter(x_values, y_values, marker='x', c='red', label='data points')
        plt.plot(x_values, y, color='red', label='y = {} x + {}'.format(slope, intercept))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Using Algebra Least Squares')
        plt.legend()
        plt.show()
    else:
        df = pd.read_csv(file_name)
        x_values = df['x'].tolist()
        y_values = df['y'].tolist()
        slope, intercept = least_sq(file_name=file_name)
        y = [slope * x_val + intercept for x_val in x_values]
        plt.scatter(x_values, y_values, marker='v', c='green', label='data points')
        plt.plot(x_values, y, color='green', label='y = {} x + {}'.format(slope, intercept))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Using Matrix Least Squares')
        plt.legend()
        plt.show()


######## TEST CASES ########
# this test case is the same as the one in 
csv_file = "data2.csv"

m1, b1 = least_sq(csv_file)
print("Slope using algebraic least squares:", m1)
print("y-intercept using algebraic least squares:", b1)
print()

m2, b2 = mat_least_sq(csv_file)
print("Slope using linear algebra least squares:", m2)
print("y-intercept using linear algebra least squares:", b2)
print()

y1 = predict(csv_file, 100)  # extrapolation
print("Extrapolation:", y1)
y2 = predict(csv_file, 38)  # interpolation
print("Interpolation:", y2)

plot_reg(csv_file, False)

plot_reg(csv_file, True)
