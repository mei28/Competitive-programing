n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [(a, b, -i-1, a + b) for i, (a, b) in enumerate(zip(A, B))]

C = list(sorted(C, key=lambda x: (x[0], x[2]), reverse=True))

ans = []
for i in range(x):
    ans.append(C[i][2])
for i in range(x):
    C.pop(0)


C = list(sorted(C, key=lambda x: (x[1], x[2]), reverse=True))
for i in range(y):
    ans.append(C[i][2])
for i in range(y):
    C.pop(0)

C = list(sorted(C, key=lambda x: (x[3], x[2]), reverse=True))
for i in range(z):
    ans.append(C[i][2])
for i in range(z):
    C.pop(0)

ans.sort(reverse=True)

for a in ans:
    print(abs(a))


