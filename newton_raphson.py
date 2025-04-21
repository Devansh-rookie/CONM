def f(x):
    return x**3 - 2*x - 17

def fdash(x):
    return 3*(x)**2 - 2

accuracy = 1e-15

x0 = eval(input("initial points: "))
itera = 0

while(True):
    if fdash(x0) == 0:  # Avoid division by zero
        print("Derivative is zero, Newton-Raphson method fails.")
        break
    x1 = x0 - f(x0)/fdash(x0)
    itera+=1
    if abs(x1 - x0) < accuracy:  # Convergence check
        break

    x0 = x1

print(f"root at found at {x1}\nin {itera} iterations")
