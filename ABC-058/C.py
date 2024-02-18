n = int(input())
S = [input() for _ in range(n)]

mat = [[0 for i in range(n)] for i in range(ord("z") - ord("a") + 1)]

for i in range(n):
    s = S[i]
    for j in s:
        tmp = ord(j) - ord("a")
        mat[tmp][i] += 1

ans = ""
for j, m in enumerate(mat):
    min_ = min(m)
    ans += chr(j + ord("a")) * min_

print(ans)
