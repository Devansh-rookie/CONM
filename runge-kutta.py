def runge_kutta_4(f, x0, y0, h, n_steps):
    """
    4th-order Runge-Kutta method for solving dy/dx = f(x, y)

    Parameters:
    - f: function f(x, y)
    - x0: initial x value
    - y0: initial y value
    - h: step size
    - n_steps: number of steps to take

    Returns:
    - Lists of x and y values
    """
    x = x0
    y = y0
    x_values = [x]
    y_values = [y]

    for _ in range(n_steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


# Define the differential equation
def f(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
n_steps = int(1/h)

# Solve using RK4
x_vals, y_vals = runge_kutta_4(f, x0, y0, h, n_steps)

# Print the results
for xi, yi in zip(x_vals, y_vals):
    print(f"x = {xi:.2f}, y = {yi:.5f}")
