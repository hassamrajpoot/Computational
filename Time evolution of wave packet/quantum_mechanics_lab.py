import numpy as np
from matplotlib import pyplot as plt
from math import sqrt , pi 
from mpmath import exp
from scipy.constants import hbar as hbar
# two_d_array = []
# for row in range(10):
#     two_d_array.append([row]*10)
#     two_d_array.append([i for i in range(10)])
# two_d_array = np.array(two_d_array)
# two_d_array = two_d_array * 10
# two_d_array = two_d_array - 5
# print(two_d_array)
# plt.imshow(two_d_array)
# plt.show()

# complex_array = []
# def wave_fun(r_value):
#     sigma = 0.1
#     a = 1/ ((sqrt(sigma)) * (pow(pi, 1/4)))
#     b = 1/ exp((r_value)**2/2*sigma**2)
#     return a * b
# x = [i for i in range(-100,100)]
# wave_fun_value = [wave_fun(i) for i in x]
# plt.plot(x, [abs(i) for i in wave_fun_value], 'r')
# def transformed_wave_fun(k_value):
#     sigma = 0.1
#     a = sqrt(sigma) / (pow(pi, 1/4)) 
#     b = 1/ exp((k_value**2 * sigma**2)/2)
#     return a * b
# new_x = [i for i in range(-100,100)]
# new_wave_fun_value = [transformed_wave_fun(i) for i in new_x]
# plt.plot(new_x, [abs(i) for i in new_wave_fun_value], 'g')
# plt.show()      

def absolute_value_squared_time_evolved_psi(t, position):
    sigma = 0.01
    m = (10^-15)
    a = pow((1/pi)*(1/sigma**2), 1/2)
    common_term = ((hbar * t)/ (m * sigma**2))
    b = 1 / pow((1+(common_term**2)), 1/2)
    c = 1 / exp((position**2/sigma**2)*(1/(1+(common_term**2))))
    return a*b*c
print(absolute_value_squared_time_evolved_psi(0, 1))

position_values = [i for i in range(-100, 100)]
absolute_values_squared_time_evolved_psi = []
time = 0
for pos in position_values:
    absolute_values_squared_time_evolved_psi.append(absolute_value_squared_time_evolved_psi(time, pos))
plt.plot(position_values, absolute_values_squared_time_evolved_psi)
plt.show()
    