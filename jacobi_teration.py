def calc_stuff(deno, positive_const, const_list, var_list, skip_index):
    # first calculate the thing to subtract
    to_sub = 0
    n = len(var_list)
    for i in range(0, n):
        if(i != skip_index):
            to_sub += const_list[i]*var_list[i]

    ans = (positive_const - to_sub)/deno;
    return ans

def jacobi(A, b):
    var_list = [0]*len(A)
    n = len(A)
    new_list = [0]*n;
    # transposed = [[row[i] for row in A]
    #              for i in range(len(A[0]))]
    for _ in range(0, 100):
        for i in range(0, n):
            new_list[i] = calc_stuff(A[i][i], b[i], A[i], var_list, i)

        var_list = new_list
    return var_list

def rearragement_diagonaly_dominant(A, b):
    newA = A
    newB = b
    n = len(A)
    dicto = {}
    dictb = {}
    # map index to diagonally dominant
    for i in range(0, n):
        for j in range(0, n):
            letele = A[i][j]
            sumaa = 0
            for k in range(0, n):
                sumaa += abs(A[i][k])
            sumaa -= letele

            if letele >= sumaa:
                if(i not in dicto):
                    dicto[j] = A[i]
                    dictb[j] = b[i]
                else:
                    return None, None
                break


    # now just rearrage

    for (index, row) in dicto.items():
        newA[index] = row

    for index, val in dictb.items():
        newB[index] = val

    return newA, newB


A = [[20, 1, -2], [3, 20, -1], [2, -3, 20]]
B = [17, -18, 25]
#
# A = [[1, 12, 3], [5, 12, 124], [199, 1, 2]]
# B = [10, 120, 3]

A, B = rearragement_diagonaly_dominant(A, B)

if(A is None):
    print("Can't be converted")
    exit(0)

vals = jacobi(A, B)

for i in vals:
    print(i, end=" ")
