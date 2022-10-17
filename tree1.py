class Joint:
    def __init__(self, p1, p2, l):
        self.p1 = p1
        self.p2 = p2
        self.l = l


f = open("2.txt")
j = []
s = f.readline().split()
n = 0
while len(s) > 0:
    j.append(Joint(int(s[0]), int(s[1]), int(s[2])))
    if int(s[0]) > n:
        n = int(s[0])
    if int(s[1]) > n:
        n = int(s[1])
    s = f.readline().split()
j.sort(key=lambda x: x.l, reverse=False)
n += 1

p = []
for i in range(n):
    p.append(i)

i = 0
k = 0
while i < len(p) - 1:
    joint = j[k]
    if p[j[k].p1] != p[j[k].p2]:
        print(j[k].p1, j[k].p2, j[k].l)
        i += 1
        cmin = min(p[j[k].p1], p[j[k].p2])
        c = max(p[j[k].p1], p[j[k].p2])
        for pnt in p:
            if pnt == c:
                pnt = cmin
    k += 1
