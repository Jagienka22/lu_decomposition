import numpy as np


def pivot(matrix):
    n = np.shape(matrix)
    ID = np.identity(n[0])
    for i in range(n[0]):
        maxm = abs(matrix[i][i])
        row = i
        for j in range(i, n[0]):
            if abs(matrix[j][i]) > maxm:
                maxm = abs(matrix[j][i])
                row = j
        if i != row:
            tmp = np.copy(ID[i])
            ID[i] = ID[row]
            ID[row] = tmp
    return ID


def facto_lu(matrix):
    size_of_matrix = np.shape(matrix)
    n = size_of_matrix[0]
    U = np.zeros((n, n))
    L = np.identity(n)
    P = np.identity(n)
    for i in range(n):
        j = i
        while j < n:
            sum = 0
            for k in range(i):
                sum += (L[i][k] * U[k][j])
            U[i][j] = matrix[i][j] - sum
            if i == j and U[i][j] == 0.0:
                P = pivot(matrix)
                matrix = np.dot(P, matrix)
                print(P, "p")
                print("dzielimy przez zero", i, j)
            else:
                j += 1
        for j in range(i + 1, n):
            if i != j:
                sum = 0
                for k in range(i):
                    sum += (L[j][k] * U[k][i])
                L[j][i] = (matrix[j][i] - sum) / U[i][i]
    return L, U, P


if __name__ == "__main__":
    n = int(input("Prosze podac rozmiar macierzy\n"))
    M = np.zeros((n, n))
    print(M)
    print("Prosze podac kolejno elementy macierzy")
    print("(w przypadku liczb dziesietnych uzywac kropki)")
    for x in range(n):
        print("Element w wierszu", x)
        m = input()
        M[x] = m.split()
    print("Wpisana macierz:\n", M, "\n")
    lu = facto_lu(M)
    L, U, P = lu
    print("L:\n ", L, "U:\n", U, "P:\n", P, "\n")
    print("Sprawdzenie: \n", np.dot(P, L, U))
