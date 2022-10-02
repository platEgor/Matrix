from math import sqrt


class Point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

jnt = []

def updatec(ix, ixmin,  c):
    for i in range(len(jnt)):
        if i != ixmin:
            if jnt[ix][i] == 1:
                p[i].c = c
                updatec(i, ix, c)


# points
f = open("1.txt")
p = []
res = []
s = f.readline().split()
i = 0
while len(s) > 0:
    p.append(Point(int(s[0]), int(s[1]), i))
    i += 1
    s = f.readline().split()


# joints
for i in range(len(p)):
    jnt.append([])
    for j in range(len(p)):
        jnt[i].append(0)


d = 0
dmin = 0
imin = 0
jmin = 0
for k in range(len(p)-1):
    f = 0
    for i in range(0, len(p)):
        for j in range(0, len(p)):
            if p[i].c != p[j].c and i != j:
                d = sqrt(pow(p[i].x - p[j].x, 2) + pow(p[i].y - p[j].y, 2))
                f += 1
                if f == 1:
                    dmin = d
                if dmin >= d:
                    dmin = d
                    imin = i
                    jmin = j
    jnt[imin][jmin] = 1
    jnt[jmin][imin] = 1
    if p[imin].c < p[jmin].c:
        updatec(jmin, imin, p[imin].c)
        p[jmin].c = p[imin].c
    else:
        if p[jmin].c < p[imin].c:
            updatec(imin, jmin, p[jmin].c)
            p[imin].c = p[jmin].c

for i in jnt:
    print(i, "\n")