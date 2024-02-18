n, m, p = map(int, input().split())
t = m
cnt = 0
for i in range(1, n + 1):
    if i == t:
        cnt += 1
        t += p
print(cnt)
