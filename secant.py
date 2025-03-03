
def f(x):
    return x**2 - 30

accuracy = 1e-7

x0,x1 = eval(input("initial points: "))
x2 = 0
# if f(x0) * f(x1) >= 0:
#     print("Invalid initial guesses. The function must have opposite signs at x0 and x1.")
#     exit(0)
itera = 0
while True:
    x2 = ((x0*f(x1) - x1*f(x0))/(f(x1) - f(x0)))
    if(abs(f(x2)) == accuracy) or (abs(x1 - x2) < accuracy):
        print(f"root at found at {x2}\nin {itera} iterations")
        break
    itera+=1
    print(f"{x0}, {x1}")
    print(f"f({x0}): {f(x0)}, f({x1}): {f(x1)}")
    x0, x1 = x1, x2
