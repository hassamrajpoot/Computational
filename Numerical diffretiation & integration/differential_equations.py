from matplotlib import pyplot
# 2. Ordinary differential Equations
# part one
# Energy of Simple harmonic oscillator = U + K = 1/2 kx2 + 1/2 mv2


def energy(displacement, velocity, mass, spring_constant):
    potential_energy = (1/2) * spring_constant * (displacement**2)
    kinetic_energy = (1/2) * mass * (velocity**2)
    Total_energy = potential_energy + kinetic_energy
    return "E = {} ".format(Total_energy)

# phi as a function of displacement = - omega2 * x


def phi_as_a_function_of_displacement(displacement, omega):
    return "\u03C6(x) = {}".format(- (omega**2) * displacement)


# Part two
# Euler's method


def eulersMethod(xn, vn, f, step):
    v_n_plus_one = vn + step * f(xn)
    x_n_plus_one = xn + step * vn
    return x_n_plus_one, v_n_plus_one


# Euler-Cromer method


def eulerCromerMethod(xn, vn, f, step):
    v_n_plus_one = vn + f(xn) * step
    x_n_plus_one = xn + vn+1 * step
    return x_n_plus_one, v_n_plus_one


# Leap Frog method


def leapFrog(xn, vn_minus_half, f, step):
    vn_plus_half = vn_minus_half + f(xn) * step
    xn_plus_one = xn + vn_plus_half * step
    return xn_plus_one, vn_plus_half


# Part three

def Euler(x0, v0, step):
    def function(omega, x):
        return -1 * (omega ** 2) * x

    k = 3.0
    m = 1.0
    omega = (k / m) ** 0.5
    x = []
    v = []
    t = []
    i = 0
    while i <= 100:
        s = step
        t.append(round(i, 3))
        i = i + s
    x.append(x0)
    v.append(v0)
    for i in range(1, len(t)):
        ind = i - 1
        vn = v[ind] + step * function(omega, x[ind])
        xn = x[ind] + step * v[ind]

        x.append(round(xn, 4))
        v.append(round(vn, 4))
    pyplot.plot(t, x, color="purple")
    pyplot.plot(t, v)
    pyplot.xlabel("t")
    pyplot.ylabel("displacement and velocity")
    pyplot.legend(["displacement", "velocity"])
    pyplot.show()


def EulerCromer(x0, v0, step):
    def function(omega, x):
        return -1 * (omega ** 2) * x

    k = 3.0
    m = 1.0
    omega = (k / m) ** 0.5
    x = []
    v = []
    t = []
    i = 0
    while i <= 100:
        s = step
        t.append(round(i, 3))
        i = i + s
    x.append(x0)
    v.append(v0)
    for i in range(1, len(t)):
        vn = v[i - 1] + step * function(omega, x[i - 1])
        xn = x[i - 1] + step * vn
        x.append(xn)
        v.append(vn)
    pyplot.plot(t, x, color="green")
    pyplot.plot(t, v)
    pyplot.xlabel("t")
    pyplot.ylabel("displacement and velocity")
    pyplot.legend(["displacement", "velocity"])
    pyplot.show()


def LeapFrog(x0, v0, step):
    def function(omega, x):
        return -1 * (omega ** 2) * x

    k = 3.0
    m = 1.0
    omega = (k / m) ** 0.5
    x = []
    v = []
    t = []
    i = 0
    while i <= 100:
        s = step
        t.append(round(i, 3))
        i = i + s
    x.append(x0)
    v.append(v0)
    for i in range(0, len(t)):
        vn = v[i] + function(omega, x[i]) * (step / 2)
        xn = x[i] + vn * step
        v.append(vn)
        x.append(xn)
    x.remove(x[-1])
    v.remove(v[-1])
    pyplot.plot(t, x, color="red")
    pyplot.plot(t, v)
    pyplot.xlabel("t")
    pyplot.ylabel("displacement and velocity")
    pyplot.legend(["displacement", "velocity"])
    pyplot.show()


def RelativeErrors(x0, v0):
    E_not = (1 / 2) * 3 * x0 ** 2 + (1 / 2) * 1 * v0 ** 2
    step = 0.01

    def Eulers():
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 100:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            ind = i - 1
            vn = v[ind] + step * function(omega, x[ind])
            xn = x[ind] + step * v[ind]

            x.append(round(xn, 4))
            v.append(round(vn, 4))
        E_as_function_of_t = []
        for a in range(0, len(x)):
            e = 0.5 * 3 * x[a] ** 2 + 0.5 * 1 * v[a] ** 2
            E_as_function_of_t.append(e)
        delta_E = []
        for num in E_as_function_of_t:
            delta_E.append((num - E_not) / E_not)
        delta_E_over_E_not = []
        for n in delta_E:
            delta_E_over_E_not.append(n / E_not)
        return [t, delta_E_over_E_not]

    def EulerCromer():
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 100:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            vn = v[i - 1] + step * function(omega, x[i - 1])
            xn = x[i - 1] + step * vn
            x.append(xn)
            v.append(vn)
        E_as_function_of_t = []
        for a in range(0, len(x)):
            e = 0.5 * 3 * x[a] ** 2 + 0.5 * 1 * v[a] ** 2
            E_as_function_of_t.append(e)
        delta_E = []
        for num in E_as_function_of_t:
            delta_E.append((num - E_not) / E_not)
        delta_E_over_E_not = []
        for n in delta_E:
            delta_E_over_E_not.append(n / E_not)
        return [t, delta_E_over_E_not]

    euler = Eulers()[1]
    eulerCromer = EulerCromer()[1]
    time = Eulers()[0]
    pyplot.plot(time, euler)
    pyplot.plot(time, eulerCromer)
    pyplot.legend(["Euler's method", "Euler-Cromer method"])
    pyplot.show()


# Part four


def Evolution_through_Eulers_method():
    def New_Euler(x0, v0, step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            ind = i - 1
            vn = v[ind] + step * function(omega, x[ind])
            xn = x[ind] + step * v[ind]
            x.append(round(xn, 4))
            v.append(round(vn, 4))
        Energy_at_Two_point_five = 0.5 * 3 * x[-1] ** 2 + 0.5 * 1 * v[-1] ** 2
        return Energy_at_Two_point_five

    t = [0.001, 0.003, 0.005, 0.007, 0.01, 0.02]
    for h in range(0, len(t)):
        print("Energy at T=2.5 s at \u0394t = {} is {}".format(t[h], New_Euler(2.0, 1.0, t[h])))


def Evolution_through_Euler_cromer_method():
    def New_EulerCromer(x0, v0, step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            vn = v[i - 1] + step * function(omega, x[i - 1])
            xn = x[i - 1] + step * vn
            x.append(xn)
            v.append(vn)
        Energy_at_Two_point_five = 0.5 * 3 * x[-1] ** 2 + 0.5 * 1 * v[-1] ** 2
        return Energy_at_Two_point_five

    t = [0.001, 0.003, 0.005, 0.007, 0.01, 0.02]
    for h in range(0, len(t)):
        print("Energy at T=2.5 s at \u0394t = {} is {}".format(t[h], New_EulerCromer(2.0, 1.0, t[h])))


def Evolution_through_leapfrog_method():
    def New_LeapFrog(x0, v0, step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(0, len(t)):
            vn = v[i] + function(omega, x[i]) * (step / 2)
            xn = x[i] + vn * step
            v.append(vn)
            x.append(xn)
        x.remove(x[-1])
        v.remove(v[-1])
        Energy_at_Two_point_five = 0.5 * 3 * x[-1] ** 2 + 0.5 * 1 * v[-1] ** 2
        return Energy_at_Two_point_five

    t = [0.001, 0.003, 0.005, 0.007, 0.01, 0.02]
    for h in range(0, len(t)):
        print("Energy at T=2.5 s at \u0394t = {} is {}".format(t[h], New_LeapFrog(2.0, 1.0, t[h])))

# Relative errors Vs delta T graphs


def Error_Vs_del_T_for_Eulers_and_EulerCromer_and_Leapfrog_method():
    del_errors_euler = []
    del_errors_euler_cromer = []
    del_errors_leapfrog = []
    del_T = []
    E_not = 0.5 * 3 * 4 + 0.5 * 1 * 1
    steps = [0.001, 0.003, 0.005, 0.007, 0.01, 0.02]
    x0 = 2.0
    v0 = 1.0

    def Eulers(step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            ind = i - 1
            vn = v[ind] + step * function(omega, x[ind])
            xn = x[ind] + step * v[ind]

            x.append(round(xn, 4))
            v.append(round(vn, 4))
        E_as_function_of_t = []
        for a in range(0, len(x)):
            e = 0.5 * 3 * x[a] ** 2 + 0.5 * 1 * v[a] ** 2
            E_as_function_of_t.append(e)
        delta_E = []
        for num in E_as_function_of_t:
            delta_E.append((num - E_not) / E_not)
        return delta_E
    for step in steps:
        l = Eulers(step)
        e = sum(l) / len(l)
        del_errors_euler.append(e)
    del_T = steps

    def EulerCromer(step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(1, len(t)):
            vn = v[i - 1] + step * function(omega, x[i - 1])
            xn = x[i - 1] + step * vn
            x.append(xn)
            v.append(vn)
        E_as_function_of_t = []
        for a in range(0, len(x)):
            e = 0.5 * 3 * x[a] ** 2 + 0.5 * 1 * v[a] ** 2
            E_as_function_of_t.append(e)
        delta_E = []
        for num in E_as_function_of_t:
            delta_E.append((num - E_not) / E_not)
        return delta_E
    for step1 in steps:
        l = EulerCromer(step1)
        e1 = sum(l) / len(l)
        del_errors_euler_cromer.append(e1)

    def LeapFrog(step):
        def function(omega, x):
            return -1 * (omega ** 2) * x

        k = 3.0
        m = 1.0
        omega = (k / m) ** 0.5
        x = []
        v = []
        t = []
        i = 0
        while i <= 2.5:
            s = step
            t.append(round(i, 3))
            i = i + s
        x.append(x0)
        v.append(v0)
        for i in range(0, len(t)):
            vn = v[i] + function(omega, x[i]) * (step / 2)
            xn = x[i] + vn * step
            v.append(vn)
            x.append(xn)
        x.remove(x[-1])
        v.remove(v[-1])
        E_as_function_of_t = []
        for a in range(0, len(x)):
            e = 0.5 * 3 * x[a] ** 2 + 0.5 * 1 * v[a] ** 2
            E_as_function_of_t.append(e)
        delta_E = []
        for num in E_as_function_of_t:
            delta_E.append((num - E_not) / E_not)
        return delta_E

    for step2 in steps:
        l = LeapFrog(step2)
        e2 = sum(l) / len(l)
        del_errors_leapfrog.append(e2)

    pyplot.plot(del_T, del_errors_euler)
    pyplot.plot(del_T, del_errors_euler_cromer)
    pyplot.plot(del_T, del_errors_leapfrog)
    pyplot.legend(["Eulers method", "Euler-Cromer method", "Leapfrog method"])
    pyplot.show()


