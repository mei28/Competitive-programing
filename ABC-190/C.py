N, M = map(int, input().split())

conditions = []

for i in range(M):
    a, b = map(int, input().split())
    conditions.append((a, b))

K = int(input())

people = []
for i in range(K):
    c, d = map(int, input().split())
    people.append((c, d))

ans = 0

cnt = [0] * 110
for bit in range(1 << K):
    for i in range(K):
        cnt[people[i][(bit >> i) % 2]] += 1

    tmp = 0
    for a, b in conditions:
        if cnt[a] > 0 and cnt[b] > 0:
            tmp += 1

    ans = max(ans, tmp)

    for i in range(K):
        cnt[people[i][(bit >> i) % 2]] -= 1

print(ans)
