N, X, T = map(int, input().split())

if N // X == N / X:
    t = N//X
else:
    t = N//X + 1

print(t*T)