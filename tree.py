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

f = open("1.txt")
p = []
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
            j.append(Joint(i, k, ((p[i].x - p[k].x, 2)**2 + (p[i].y - p[k].y, 2)**2)**0.5))
j.sort(key=lambda x: x.l, reverse=False)

i = 0
k = 0
while i < len(p) - 1:
    joint = j[k]
    if p[j[k].p1].c != p[j[k].p2].c:
        print(j[k].p1, j[k].p2, j[k].l)
        i += 1
        cmin = min(p[j[k].p1].c, p[j[k].p2].c)
        c = max(p[j[k].p1].c, p[j[k].p2].c)
        for pnt in p:
            if pnt.c == c:
                pnt.c = cmin
    k += 1
