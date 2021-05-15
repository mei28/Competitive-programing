N = int(input())
A = []
for i in range(N):
    tmp = input().split()
    s, t = tmp[0], tmp[1]
    t = int(t)
    A.append([s, t])

A = list(sorted(A, key=lambda x: x[1]))
print(A[-2][0])
