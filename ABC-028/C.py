a, b, c, d, e = map(int, input().split())
T = set()

A = [a, b, c, d, e]
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            tmp = A[i] + A[j] + A[k]
            T.add(tmp)
T = list(T)
T.sort()
print(T[-3])
