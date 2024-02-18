# S = input()
# N = int(input())
k, N = map(int, input().split())
S = input()

nex = [[0 for _ in range(100100)] for _ in range(26)]

# 前処理を行う
# dp[i][j]: 前からi文字列の右の部分文字列のうち，一番左にある文字jのインデックス

for i in range(26):
    nex[len(S)][i] = len(S)

for i in range(len(S) - 1, -1, -1):
    for j in range(26):
        if int(ord(S[i]) - ord("a")) == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i + 1][j]


# 一文字ずつ貪欲に決める

ans = ""
current_pos = 0

for i in range(N):
    for j in range(26):
        next_pos = nex[current_pos][j]
        max_possible_length = len(S) - next_pos + i
        if max_possible_length >= N:
            ans += chr(ord("a") + j)
            current_pos = next_pos + 1
            break

print(ans)
