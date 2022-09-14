def det(x):
    lenx = len(x)
    if lenx == 1:
        return x[0][0]
    else:
        d = 0
        for i in range(lenx):
            y = []
            for j in range(1, lenx):
                y.append([])
                for k in range(lenx):
                    if k != i:
                        y[j - 1].append(x[j][k])
            d += x[0][i] * det(y) * ((-1) ** i)
        return d


a3 = [[6, 7, 3], [10, 9, 5], [2, 1, 8]]
a4 = [[6, 7, 3, 9], [10, 9, 5, 1], [2, 1, 8, 11], [1, 3, 7, 4]]
print(det(a4))
