d = int(input())
n = int(input())

V = [0] * (d + 2)

for _ in range(n):
    l, r = map(int, input().split())
    V[l] += 1
    V[r + 1] += -1

for i in range(len(V)):
    if 0 < i:
        V[i] += V[i - 1]
print(*V[1 : d + 1])
