n = int(input())
P = list(map(int, input().split()))
q = []
for i in range(n):
    q.append([P[i], i + 1])

q.sort()
ans = []

for i in q:
    ans.append(i[1])

print(*ans)
