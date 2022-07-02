n, x = map(int, input().split())
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

A = ""
for a in alp:
    A += a * n

print(A[x - 1])
