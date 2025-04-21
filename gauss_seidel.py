def gauss_seidel(A, b, accuracy=1e-6, max_iterations=100):
    n = len(A)
    x = [0.0] * n  # Initial guess

    for _ in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))      # Use updated values
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))   # Use old values
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        # Convergence check
        if all(abs(x_new[i] - x[i]) < accuracy for i in range(n)):
            return x_new

        x = x_new

    print("Max iterations reached without convergence.")
    return x


A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]

b = [4, 7, 3]

solution = gauss_seidel(A, b)

print("Solution:")
for val in solution:
    print(f"{val:.6f}", end=" ")
