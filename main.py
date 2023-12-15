l1 = input().split(" ")
l2 = input().split(" ")
l1, l2 = [eval(i) for i in l1], [eval(i) for i in l2]

steal = l1[1] / 2
baskets = l1[1]

while True:
    sub = l2.copy()
    for i in range(int(steal)):
        sub.pop(sub.index(max(sub)))
        if len(sub) == 0:
            sub.append(0)

    split = max(l2) / 2
    if (2 * split) % 2 == 0:
        split_n = [split, split]
    else:
        split_n = [split - .5, split + .5]

    l3 = l2.copy()
    l3.pop(l3.index(max(l3)))
    for i in range(2):
        l3.append(int(split_n[i]))
    temp = l3.copy()

    z = 0
    y = 0
    for i in range(int(steal)):
        if len(l3) == 0:
            l3.append(0)
            break
        z += max(l3)
        l3.pop(l3.index(max(l3)))
        if len(sub) == 0:
            sub.append(0)
            break
        y += max(sub)
        sub.pop(sub.index(max(sub)))

    if z > y:
        l2 = temp
    else:
        break

# Does steals
for i in range(int(steal)):
    l2.pop(l2.index(max(l2)))

# Counts points
x = 0
for i in range(int(steal)):
    if len(l2) == 0:
        break
    x += max(l2)
    l2.pop(l2.index(max(l2)))
print(x)
