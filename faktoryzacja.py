import numpy as np
import sys


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
                tmp_P = pivot(matrix)
                P = np.dot(P, tmp_P)
                matrix = np.dot(tmp_P, matrix)
            else:
                j += 1
        for j in range(i + 1, n):
            if i != j:
                sum = 0
                for k in range(i):
                    sum += (L[j][k] * U[k][i])
                L[j][i] = (matrix[j][i] - sum) / U[i][i]
    return L, U, P

def check_if_float(element):
    try:
        float(element)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    n = int(input("Prosze podac rozmiar macierzy\n"))
    M = np.zeros((n, n))
    print("Prosze podac kolejno elementy macierzy")
    print("(w przypadku liczb dziesietnych uzywac kropki)")
    for x in range(n):
        print("Element w wierszu", x)
        m = input()
        i = 0
        for y in m.split():
            if check_if_float(y):
                M[x][i] = y
                i += 1
            else:
                print("Ktorys z elementow z wiersza nie jest liczba. Uruchom program jeszcze raz")
                sys.exit()

    print("Wpisana macierz:\n", M, "\n")
    lu = facto_lu(M)
    L, U, P = lu
    print("L:\n", L, "\nU:\n", U, "\nP:\n", P, "\n")
    w = np.dot(P, L)
    print("\nSprawdzenie PxLxU: \n", np.dot(w, U))
    print("Poczatkowa macierz:\n", M)
