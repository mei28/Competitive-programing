n, m = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if all([S[i][k] == "o" or S[j][k] == "o" for k in range(m)]):
            ans += 1
print(ans)
