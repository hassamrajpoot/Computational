import numpy as np
import matplotlib.pyplot as plt

L = 1.0
V0 = 0.0
Vext = 10000.0


# function of the energy
def factor(E, x):
    if x < L:
        V = V0
    else:
        V = Vext
    return -2.0 * (E - V)


def function(x, psi, der_psi, E):
    a = factor(E, x)
    return a * psi


nx = 1001
dx = float(input("Enter step size here :"))

# Initial conditions for the integration
# Even solutions
psi0 = 1.0
der_psi0 = 0.0
# Odd solutions
# psi0     = 0.0
# der_psi0 = 1.0

# Build array of the wave function
psi = np.zeros(nx)
x = np.zeros(nx)

# Set initial values
psi[0] = psi0
der_psi = der_psi0

# Initialize position array
x0 = 0.0
x[0] = x0
for ix in range(nx - 1):
    x[ix + 1] = x[ix] + dx
# Start first shooting loop with Euler
print('Initial conditions are:')
print(' Psi(0)    :', psi[0])
print(' der_psi(0):', der_psi)

# Compute first ne eigenvalues and plot corresponding eigenfunctions.
ne = 3

# Set initial energy to
E = 0.0

# Start the loops on the eigen values
for ie in range(ne):
    # Initialize energy variation and accuracy
    de = 0.1
    e_cut = 1.0e-5
    # Initialize first energy from previous
    E = E + de
    # Do a first shooting with energy:
    psi[0] = psi0
    der_psi = der_psi0
    for ix in range(nx - 1):
        k1 = dx * der_psi0
        l1 = dx * function(x0, psi0, der_psi0, E)
        k2 = dx * (der_psi0 + (l1 / 2))
        l2 = dx * function((x0 + (dx / 2)), (psi0 + (k1 / 2)), (der_psi0 + (l1 / 2)), E)
        k3 = dx * (der_psi0 + (l2 / 2))
        l3 = dx * function((x0 + (dx / 2)), (psi0 + (k2 / 2)), (der_psi0 + (l2 / 2)), E)
        k4 = dx * (der_psi0 + l3)
        l4 = dx * function((x0 + dx), (psi0 + k3), (der_psi0 + l3), E)
        psi[ix + 1] = psi[ix] + (1 / 6) * (k1 + k2 + k3 + k4)
        der_psi = der_psi + (1 / 6) * (l1 + l2 + l3 + l4)

    # Store value of the wave function in x=L
    # We need it to compare the signs!
    psi_old = psi[nx - 1]

    while abs(de) >= e_cut:
        psi[0] = psi0
        der_psi = der_psi0

        for ix in range(nx - 1):
            k1 = dx * der_psi0
            l1 = dx * function(x0, psi0, der_psi0, E)
            k2 = dx * (der_psi0 + (l1 / 2))
            l2 = dx * function((x0 + (dx / 2)), (psi0 + (k1 / 2)), (der_psi0 + (l1 / 2)), E)
            k3 = dx * (der_psi0 + (l2 / 2))
            l3 = dx * function((x0 + (dx / 2)), (psi0 + (k2 / 2)), (der_psi0 + (l2 / 2)), E)
            k4 = dx * (der_psi0 + l3)
            l4 = dx * function((x0 + dx), (psi0 + k3), (der_psi0 + l3), E)
            psi[ix + 1] = psi[ix] + (1 / 6) * (k1 + k2 + k3 + k4)
            der_psi = der_psi + (1 / 6) * (l1 + l2 + l3 + l4)

        # Check sign variation (did we cross an eigenvalue?)
        if psi_old * psi[nx - 1] < 0:
            de = -0.1 * de
        # Update energy
        E = E + de
        # Store old wave function
        psi_old = psi[nx - 1]

    # Plot Eigenfunction
    plt.plot(x, psi, 'b--', label='E_{} : {}'.format(ie, E))
    # print eigenvalue
    print('E_{} : {}'.format(ie, E))

# Print final picture
plt.legend()
plt.axis([0, L, -1.0, 1.0])
plt.xlabel('x')
plt.ylabel('Psi(x)')
plt.show()



