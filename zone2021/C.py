n = int(input())

specs = []
for i in range(n):
    spec = list(map(int, input().split()))
    specs.append(spec)


def ok(x):
    exist = [False] * (1 << 5)
    for spec in specs:
        binary = 0
        for i in range(5):
            if spec[i] >= x:
                binary |= 1 << i
            exist[binary] = True
    for i in range(1 << 5):
        for j in range(i + 1, 1 << 5):
            for k in range(j + 1, 1 << 5):
                if exist[i] and exist[j] and exist[k] and (i | j | k) == (1 << 5) - 1:
                    return True
    return False


bottom, top = 1, 10 ** 10

while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        bottom = mid
    else:
        top = mid

print(bottom)
