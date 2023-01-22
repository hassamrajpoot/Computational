import numpy as np
import matplotlib.pyplot as plt
import fourier as f
import solver as s


# Partial Differential Equations
# Part one


def Euler():
    t0 = 0.0  # initial time
    tf = 10000.0  # Final time
    dt = 0.1  # Time step
    nt = int((tf - t0) / dt)  # Number of time integration steps

    dx = 1.0  # Space discretization step
    nx = int(f.L / dx)
    # Amplitude of the system
    u = np.zeros((2, nx))

    # Vector for plotting
    x = np.zeros(nx)
    for ix in range(nx - 1):
        x[ix + 1] = x[ix] + dx

    # Modified Initial conditions of u in (0,L)
    u[0, 1:nx - 1] = 50.0  # Constant
    u[0] = 100.0
    u[-1] = 0.0
    # Constant
    C = f.D * dt / dx ** 2

    for it in range(nt - 1):
        u[1, 0] = u[0, 0]
        for ix in range(1, nx - 1):
            # print(C,u[0,ix-1:ix+2])
            u[1, ix] = s.eulerFourier(C, u[0, ix - 1:ix + 2])

        u[0, :] = u[1, :]
        if it % 10000 == 0:
            plot1 = plt.figure(1)
            plt.plot(x[:], u[0, :], 'b--', label='')
            # print(u)
    # plt.plot(x[:], u[0,:], 'b--',label='Position')
    plt.xlabel('x')
    plt.ylabel('u(x,t)')
    plt.scatter(f.L / 4, 50, color="black")
    plt.scatter(f.L / 2, 50, color="red")
    plt.scatter((3 / 4) * f.L, 50, color="green")
    plt.annotate("""    black --> x=L/4
    red --> x=L/2
    green --> x=3L/4""", xy=(60.3, 104))
    plt.title("Euler's method")
    plt.axis([0, 100, 0, 120])


def CrankNicolson():
    t0 = 0.0  # initial time
    tf = 10000.0  # Final time
    dt = 0.1  # Time step
    nt = int((tf - t0) / dt)  # Number of time integration steps

    dx = 1.0  # Space discretization step
    nx = int(f.L / dx)
    # Amplitude of the system
    u = np.zeros((2, nx))

    # Vector for plotting
    x = np.zeros(nx)
    for ix in range(nx - 1):
        x[ix + 1] = x[ix] + dx

    # Modified Initial conditions of u in (0,L)
    u[0, 1:nx - 1] = 50.0  # Constant
    u[0] = 100.0
    u[-1] = 0.0
    # Constant
    C = f.D * dt / dx ** 2

    for it in range(nt - 1):
        d = s.crankNicolson_d_vec(C, u[0, :])
        u[1, :] = s.thomas_alog(C, d[:])
        u[0, :] = u[1, :]
        if it % 10000 == 0:
            plot2 = plt.figure(2)
            plt.plot(x[:], u[0, :], 'b--', label='')

    plt.xlabel('x')
    plt.ylabel('u(x,t)')
    plt.scatter(f.L / 4, 50, color="black")
    plt.scatter(f.L / 2, 50, color="red")
    plt.scatter((3 / 4) * f.L, 50, color="green")
    plt.annotate("""    black --> x=L/4
    red --> x=L/2
    green --> x=3L/4""", xy=(60.3, 104))
    plt.title("Crank-Nicolson method")
    plt.axis([0, 100, 0, 120])


Euler()
CrankNicolson()
plt.show()


# Part two


def Euler(del_x, del_t):
    t0 = 0.0  # initial time
    tf = 10000.0  # Final time
    dt = del_t  # Time step
    nt = int((tf - t0) / dt)  # Number of time integration steps

    dx = del_x  # Space discretization step
    nx = int(f.L / dx)
    # Amplitude of the system
    u = np.zeros((2, nx))
    
    # Vector for plotting
    x = np.zeros(nx)
    for ix in range(nx - 1):
        x[ix + 1] = x[ix] + dx

    # Initial conditions of u in (0,L)
    u[0, 1:nx - 1] = 50.0  # Constant
    u[0] = 100.0	
    u[-1] = 0.0
    # Constant
    C = f.D * dt / dx ** 2

    for it in range(nt - 1):
        u[1, 0] = u[0, 0]
        for ix in range(1, nx - 1):
            # print(C,u[0,ix-1:ix+2])
            u[1, ix] = s.eulerFourier(C, u[0, ix - 1:ix + 2])

        u[0, :] = u[1, :]
    return u[0]


def CrankNicolson(del_x, del_t):
    t0 = 0.0  # initial time
    tf = 10000.0  # Final time
    dt = del_t  # Time step
    nt = int((tf - t0) / dt)  # Number of time integration steps

    dx = del_x  # Space discretization step
    nx = int(f.L / dx)
    # Amplitude of the system
    u = np.zeros((2, nx))
    

    # Vector for plotting
    x = np.zeros(nx)
    for ix in range(nx - 1):
        x[ix + 1] = x[ix] + dx

    # Initial conditions of u in (0,L)
    u[0, 1:nx - 1] = 50.0  # Constant
    u[0] = 100.0
    u[-1] = 0.0

    # Constant
    C = f.D * dt / dx ** 2

    for it in range(nt - 1):
        d = s.crankNicolson_d_vec(C, u[0, :])
        u[1, :] = s.thomas_alog(C, d[:])
        u[0, :] = u[1, :]
    return u[0]


def root_mean_square_deviation(del_x, del_t):
    eulers = Euler(del_x, del_t)
    cranknicolson = CrankNicolson(del_x, del_t)
    sum1 = 0
    for i in range(0, len(eulers)):
        sum1 = sum1 + (eulers[i] - cranknicolson[i]) ** 2
    sigma = (sum1 / len(eulers) * len(cranknicolson)) ** 0.5
    return sigma


def graphs():
    del_x_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    del_t_values = [0.1, 0.1, 0.1, 0.1, 0.1]
    sigma_values = []
    del_x_values1 = [6.0, 7.0, 8.0, 9.0, 10.0]
    del_t_values1 = [0.1, 0.1, 0.1, 0.1, 0.1]
    sigma_values1 = []
    for j in range(0, len(del_t_values)):
        sigma_values.append(root_mean_square_deviation(del_x_values[j], del_t_values[j]))
    for k in range(0, len(del_t_values1)):
        sigma_values1.append(root_mean_square_deviation(del_x_values1[k], del_t_values1[k]))
    pyplot.plot(del_x_values, sigma_values)
    pyplot.plot(del_x_values1, sigma_values1)
    pyplot.xlabel("\u0394x")
    pyplot.ylabel("sigma (\u03C3)")
    pyplot.show()




