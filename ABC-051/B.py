K, S = map(int, input().split())
cnt = 0

for x in range(0, K + 1):
    for y in range(0, K + 1):
        z = S - x - y
        if 0 <= z <= K:
            cnt += 1

print(cnt)
