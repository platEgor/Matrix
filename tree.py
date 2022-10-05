from math import sqrt


class Point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


class Joint:
    def __init__(self, p1, p2, l):
        self.p1 = p1
        self.p2 = p2
        self.l = l


j1 = []


def updatec(p, pmin, c):
    for i in j1:
        if i.p1 == p and i.p2 != pmin:
            i.p2.c = c
            updatec(i.p2, i.p1, c)
        elif i.p2 == p and i.p1 != pmin:
            i.p1.c = c
            updatec(i.p1, i.p2, c)


f = open("1.txt")
p = []
res = []
s = f.readline().split()
q = 0
while len(s) > 0:
    p.append(Point(int(s[0]), int(s[1]), q))
    q += 1
    s = f.readline().split()

j = []
for i in range(len(p)):
    for k in range(len(p)):
        if i > k:
            j.append(Joint(p[i], p[k], sqrt(pow(p[i].x - p[k].x, 2) + pow(p[i].y - p[k].y, 2))))
j = sorted(j, key=lambda x: x.l, reverse=True)
lenj = len(j) - 1

i = 0
while i < len(p) - 1:
    joint = j[lenj]
    if joint.p1.c != joint.p2.c:
        j1.append(joint)
        print(joint.l)
        i += 1
        if joint.p1.c > joint.p2.c:
            joint.p1.c = joint.p2.c
            updatec(joint.p1, joint.p2, joint.p2.c)
        else:
            joint.p2.c = joint.p1.c
            updatec(joint.p2, joint.p1, joint.p1.c)
    lenj -= 1
