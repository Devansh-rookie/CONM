def f(x):
    return x**3 - 17

accuracy = 1e-10

x0,x1 = eval(input("initial points: "))
x2 = 0
if f(x0) * f(x1) >= 0:
    print("Invalid initial guesses. The function must have opposite signs at x0 and x1.")
    exit(0)
prevx = None
itera = 0
while(abs(x0 - x1) > accuracy):
    x2 = ((x0*f(x1) - x1*f(x0))/(f(x1) - f(x0)))
    if(f(x2) == 0) or (prevx is not None and abs(x2 - prevx) < accuracy):
        print(f"root at found at {x2}\nin {itera} iterations")
        break
    prevx = x2
    itera+=1
    if(f(x2)*f(x0) < 0):
        x1 = x2
    else:
        x0 = x2

# print(f"Solution: {x2}")
