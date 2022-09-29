import random

def det(x):
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


a3 = [[6, 7, 3], [10, 9, 5], [2, 1, 8]]
a4 = [[6, 7, 3, 9], [10, 9, 5, 1], [2, 1, 8, 11], [1, 3, 7, 4]]
l = random.randint(1, 5)
a = []
for i in range(l):
    a.append([])
    for j in range(l):
        a[i].append(random.randint(0, 50))
print(a)
print(det(a))
