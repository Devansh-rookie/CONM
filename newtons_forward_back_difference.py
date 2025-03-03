# import math
def forward_difference(initial_arr):
    # del y0's on the 0'th element of all
    table = [initial_arr[:]]
    n = len(initial_arr)
    for i in range(n - 1):
        node = []
        for j in range(n - i - 1):
            node.append(table[i][j+1] - table[i][j])
        table.append(node)

    return table

def forward_interpolation(initial_arr, x, x0, h):
    table = forward_difference(initial_arr)
    n = len(table) # this is the same as len(initial_arr) - 1
    p = (x - x0) / h
    ans = 0

    # direct multipication from 0 to i for pCi
    #

    term_node = 0

    for i in range(n):
        term_node = table[i][0] # forward interpolation else go from the last value
        for j in range(i):
            term_node *= (p - j)/(j+1)
        # term_node /= math.factorial(i)
        # if(i != 0): term_node *= i
        ans += term_node

    return ans

def backward_interpolation(initial_arr, x, xn, h):
    table = forward_difference(initial_arr)
    n = len(table) # this is the same as len(initial_arr) - 1
    p = (x - xn) / h
    ans = 0

    # direct multipication from 0 to i for pCi

    term_node = 0

    for i in range(n):
        term_node = table[i][len(table[i]) - 1]
        for j in range(i):
            term_node *= (p + j)/(j+1)
        ans += term_node
    return ans

x0 = 40
xn = 80
h = 10
x = 45
initial_arr = [31, 73, 124, 159, 190]
print(forward_difference(initial_arr))
print(forward_interpolation(initial_arr, x, x0, h))
print(backward_interpolation(initial_arr, x, xn, h))
