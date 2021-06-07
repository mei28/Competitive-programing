n = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    if a <= 10:
        continue
    cnt += a - 10

print(cnt)
