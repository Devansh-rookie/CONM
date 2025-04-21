def calc_stuff(denominator, rhs_value, row_coeffs, old_vars, skip_index):
    to_subtract = sum(row_coeffs[i] * old_vars[i] for i in range(len(row_coeffs)) if i != skip_index)
    return (rhs_value - to_subtract) / denominator

def jacobi(A, b, max_iterations=100, tolerance=1e-9):
    n = len(A)
    x_old = [0.0] * n
    x_new = [0.0] * n

    for _ in range(max_iterations):
        for i in range(n):
            x_new[i] = calc_stuff(A[i][i], b[i], A[i], x_old, i)

        # Optional: Convergence check
        if all(abs(x_new[i] - x_old[i]) < tolerance for i in range(n)):
            break

        x_old = x_new[:]

    return x_new

def rearrange_diagonally_dominant(A, b):
    n = len(A)
    used = [False] * n
    newA = [None] * n
    newB = [None] * n

    for target_row in range(n):
        found = False
        for i in range(n):
            if used[i]:
                continue
            diag = abs(A[i][target_row])
            off_diag_sum = sum(abs(A[i][j]) for j in range(n) if j != target_row)
            if diag >= off_diag_sum:
                newA[target_row] = A[i]
                newB[target_row] = b[i]
                used[i] = True
                found = True
                break
        if not found:
            return None, None

    return newA, newB

A = [[20, 1, -2], [3, 20, -1], [2, -3, 20]]
B = [17, -18, 25]

A, B = rearrange_diagonally_dominant(A, B)

if A is None:
    print("Can't be converted to diagonally dominant form.")
    exit(0)

solution = jacobi(A, B)

print("Solution:")
for val in solution:
    print(f"{val:.6f}", end=" ")
