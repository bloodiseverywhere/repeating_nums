a = [int(i) for i in input().split()]
c = 0
a.sort()
res = []
for j in range(len(a)):
    if len(a) == 1:
        break
    if (a[j]) == (a[j-1]) and a[j] not in res:
        res.append(a[j])
print(*res)
