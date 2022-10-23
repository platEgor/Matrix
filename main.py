import random


def det(x):
    """
    returns the determinant of a matrix
    :param x: list of lists of real numbers (matrix)
    :return: real (determinant)
    """
    lenx = len(x)
    if lenx == 1:
        return x[0][0]
    else:
        d = 0
        for i in range(lenx):
            y = []
            for i1 in range(lenx - 1): y.append([])
            for j in range(lenx):
                if j != i:
                    for k in range(1, lenx):
                        y[k - 1].append(x[k][j])
            d += x[0][i] * det(y) * ((-1) ** i)
        return d


# A - coefficients. B - constants. l - number of equations and roots
l = random.randint(1, 5)
A = []
B = []
X = []

# fill A, B with random numbers
for i in range(l):
    A.append([])
    B.append(random.randint(0, 50))
    for j in range(l):
        r = random.randint(0, 50)
        A[i].append(r)

# the part where we calculate the roots
for i in range(l):
    AI = []
    for j in range(l):
        AI.append([])
        for k in range(l):
            if k == i:
                AI[j].append(B[j])
            else:
                AI[j].append(A[j][k])
    X.append(det(AI) / det(A))

# print all
for i in range(l):
    print(A[i], B[i])
print(X)
