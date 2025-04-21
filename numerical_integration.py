import math

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    return h * result


def simpsons_one_third(f, a, b, n):
    if n % 2 != 0:
        return None

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        coeff = 4 if i % 2 != 0 else 2
        result += coeff * f(x)

    return (h / 3) * result


def simpsons_three_eighth(f, a, b, n):
    if n % 3 != 0:
        return None

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        coeff = 3 if i % 3 != 0 else 2
        result += coeff * f(x)

    return (3 * h / 8) * result


def f(x):
    return math.exp(-x ** 2)

a = 0
b = 1
n1 = 10  # For Simpson's 1/3 (must be even)
n2 = 9   # For Simpson's 3/8 (must be multiple of 3)
n = 10
approx = trapezoidal(f, a, b, n)
result_1_3 = simpsons_one_third(f, a, b, n1)
result_3_8 = simpsons_three_eighth(f, a, b, n2)

print(f"Trapezoidal Rule Result: {approx:.6f}")
print(f"Simpson's 1/3 Rule Result: {result_1_3:.6f}")
print(f"Simpson's 3/8 Rule Result: {result_3_8:.6f}")
