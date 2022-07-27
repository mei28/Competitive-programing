n = int(input())
A = list(map(int, input().split()))

L = [0] * (max(A) + 10)

for a in A:
    for i in [-1, 0, 1]:
        na = a + i
        L[na] += 1

print(max(L))
