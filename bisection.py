import math

def bisection(f, a, b, accuracy=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("f(a) and f(b) should have opposite signs.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < accuracy or (b - a) / 2 < accuracy:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Maximum iterations reached without convergence.")
    return None

# f(x) = x^3 - x - 2
def func(x):
    return x**3 - x - 2

root = bisection(func, 1, 2)

if root is not None:
    print(f"Root found: {root:.6f}")
