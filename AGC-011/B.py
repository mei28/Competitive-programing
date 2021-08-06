n = int(input())
A = list(map(int, input().split()))
A.sort()
csum = [0] * (n + 1)

for i in range(n):
    csum[i + 1] = csum[i] + A[i]


start = 0
now = 1

while True:
    if now == n:
        break
    if csum[now] * 2 >= A[now]:
        now += 1
    else:
        start = now
        now += 1

print(n - start)
