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
    if max(split_n) >= max(sub) and max(l2) > 1:
        l2.pop(l2.index(max(l2)))
        for i in range(2):
            l2.append(int(split_n[i]))
    else:
        break

for i in range(int(steal)):
    l2.pop(l2.index(max(l2)))

x = 0
for i in range(int(steal)):
    x += max(l2)
    l2.pop(l2.index(max(l2)))
print(x)
