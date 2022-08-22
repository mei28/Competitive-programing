n, m, t = map(int, input().split())
A = list(map(int, input().split()))
dct = {}

for _ in range(m):
    x, y = map(int, input().split())
    dct[x - 1] = y

for i, a in enumerate(A):
    if i in dct.keys():
        t += dct[i]
    t -= a
    if t <= 0:
        print("No")
        exit()

print("Yes")
