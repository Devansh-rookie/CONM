from sympy import *
# print(integrate(exp(x)**2, x))
#

accuracy = 1e-6

def picards_method(f, x0, y0, n, finx):
    x, y = symbols('x y')
    y_values = [y0]
    it = 0
    for i in range(n):
        y_next = y0 + integrate(f.subs(y, y_values[-1]), (x, x0, finx))
        y_values.append(y_next)
        it+=1
        if abs(y_next - y_values[-2]) < accuracy:
            break
    return it, y_values[-1]

x, y = symbols('x y')

# Given ODE: y' = x**2 - y**2
f = x**2 - y**2

x0 = 0
y0 = 0
finx = 0.3 # final x

print(picards_method(f, x0, y0, 1000, finx))
