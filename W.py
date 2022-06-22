import math

ynot = 1
tnot = 0
t1 = tnot
y1 = ynot

h1 = 0.1


l1 = []

l1.append(ynot)

for i in l1:
    if t1 < .4:
        slope = 3 + t1 - y1
        y1 = y1 + slope * h1
        l1.append(round(y1,4))
        t1 += h1
    else:
        break

print(l1)


t2 = tnot
y2 = ynot

h2 = 0.05


l2 = []

l2.append(ynot)

for i in l2:
    if t2 < .4:
        slope = 3 + t2 - y2
        y2 = y2 + slope * h2
        l2.append(round(y2,4))
        t2 += h2
    else:
        break

print(l2)

t3 = tnot
y3 = ynot

h3 = 0.025

l3 = []
l3.append(ynot)

for i in l3:
    if t3 < .4:
        slope = 3 + t3 - y3
        y3 = y3 + slope * h3
        l3.append(round(y3,4))
        t3 += h3
    else:
        break

print(l3)








