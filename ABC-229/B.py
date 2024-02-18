a, b = input().split()

a = a[::-1]
b = b[::-1]

n = min(len(a), len(b))

for i in range(n):
    _a, _b = int(a[i]), int(b[i])
    if _a + _b >= 10:
        print("Hard")
        exit()

print("Easy")
