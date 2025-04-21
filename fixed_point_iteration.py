def fixed_point_iteration(g, x0, tolerance=1e-6, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        x_new = g(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new

    print("Maximum iterations reached without convergence.")
    return x

import math

# Define g(x) = cos(x)
def g(x):
    return math.cos(x)

# Initial guess
x0 = 0.5

root = fixed_point_iteration(g, x0)

print(f"Root found: {root:.6f}")
