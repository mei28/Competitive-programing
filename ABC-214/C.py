n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))


time = [100000000000] * n

min_i = T.index(min(T))

time[min_i] = T[min_i]

for i in range(1, n):
    k = (i + min_i) % n
    time[k] = min(time[k - 1] + S[k - 1], T[k])

print(*time)
