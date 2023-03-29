n = int(input())
S = input()
M = [[0, 0] for _ in range(n + 1)]

# [E,W]
for i in range(n):
    s = S[i]
    if s == "E":
        M[i + 1][0] = M[i][0] + 1
        M[i + 1][1] = M[i][1] + 0
    else:
        M[i + 1][0] = M[i][0] + 0
        M[i + 1][1] = M[i][1] + 1

ans = 1 << 32
for i in range(n):
    E_left = M[i][0] - M[0][0]
    E_right = M[n][0] - M[i + 1][0]
    S_left = M[i][1] - M[0][1]
    S_right = M[n][1] - M[i + 1][1]
    ans = min(E_right + S_left, ans)
print(ans)
