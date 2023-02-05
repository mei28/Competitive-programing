n, k = map(int, input().split())
S = [input() for _ in range(k)]
S.sort()
print(*S)
