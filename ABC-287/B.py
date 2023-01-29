n, m = map(int, input().split())

S = []
T = []

for _ in range(n):
    s = input()[-3:]
    S.append(s)
for _ in range(m):
    t = input()
    T.append(t)
ans = 0
for i in range(n):
    for j in range(m):
        if S[i] == T[j]:
            ans += 1
            break
print(ans)
