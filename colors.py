from math import sqrt


class Point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


f = open("1.txt")
p = []
s = f.readline().split()
i = 0
while len(s) > 0:
    p.append(Point(int(s[0]), int(s[1]), i))
    i += 1
    s = f.readline().split()
# for i in p:
#     print(i.x, " ", i.y, " ", i.c, "\n")
mn = sqrt(pow(p[0].x - p[1].x, 2) + pow(p[0].y - p[1].y, 2))
d = 0
imin = 0
jmin = 0
for i in range(1, len(p) - 1):
    for j in range(1, len(p) - 1):
        d = sqrt(pow(p[i].x - p[j].x, 2) + pow(p[i].y - p[j].y, 2))
        if mn > d:
            mn = d
            imin = i
            jmin = j
p[imin].c = min(p[imin].c, p[jmin].c)
p[jmin].c = p[imin].c
