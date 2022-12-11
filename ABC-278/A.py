n, k = map(int, input().split())
A = list(map(int, input().split()))
A += [0] * k
print(*A[k:])
