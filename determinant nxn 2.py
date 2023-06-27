import numpy as np

# matrix = [[5, 2, 4, 3], [7, 6, 4, 1], [3, 2, 1, 4], [5, 4, 6, 4]]

matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 1]]

0
def inverse(matrix):
    n = len(matrix)
    if n == 1:
        dt = matrix[0][0]
        if dt == 0:
            print('Non-invertible matrix')
            return
    elif n == 2:
        dt = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        print("dt", dt)
        if dt == 0:
            print('Non-invertible matrix')
            return
        a = matrix[0][0]
        matrix[0][0] = matrix[1][1]
        matrix[1][1] = a
        matrix[0][1] = matrix[0][1] * (-1)
        matrix[1][0] = matrix[1][0] * (-1)
        inv_mat = []
        for i in range(n):
            for j in matrix[i]:
                j = j / dt
            i = list(matrix[i])
            inv_mat.append(i)
        inv_mat = np.array(inv_mat)
        print("inv_mat", inv_mat)
        return inv_mat
    else:
        matrix2 = []
        for r in range(n - 1):
            temp3 = []
            for c in range(n - 1):
                temp3.append(matrix[r][c])
            matrix2.append(temp3)
        matrix2 = np.array(matrix2)
        temp1 = []
        for c in range(n - 1):
            temp1.append(matrix[c][-1])
        B = np.array(temp1)
        temp2 = []
        for c in range(n - 1):
            temp2.append(matrix[-1][c])
        C = np.array(temp2)
        d = matrix[-1][-1]
        print('d', d)
        print('B', B)
        print('C', C)
        print('matrix2', matrix2)
        t = 1 / (d - np.dot(np.dot(C, inverse(matrix2)), B))
        Y = -np.dot(inverse(matrix2), B) * t
        Z = -np.dot(C, inverse(matrix2)) * t
        I = np.identity(n - 1)
        X = np.dot(inverse(matrix2), (I - np.dot(B, Z)))

        print('X', X)
        print('t', t)
        print('Y', Y)
        print('Z', Z)


inverse(matrix)
