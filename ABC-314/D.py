N = int(input())
S = list(input())
Q = int(input())
queries = [tuple(input().strip().split()) for _ in range(Q)]


# クエリを順に処理
last_idx = -1
for i, q in enumerate(queries):
    t = int(q[0])
    if t == 1:
        x, c = int(q[1]) - 1, q[2]
        S[x] = c
    elif t == 2:
        last_idx = max(last_idx, i)
    elif t == 3:
        last_idx = max(last_idx, i)

# 変換フラグがTrueであれば、全体の変換を行う
S = "".join(S)
if last_idx == -1:
    print(S)
    exit()
elif int(queries[last_idx][0]) == 2:
    S = S.lower()
elif int(queries[last_idx][0]) == 3:
    S = S.upper()

T = list(S)
for i in range(last_idx + 1, Q):
    q = queries[i]
    x, c = int(q[1]) - 1, q[2]
    T[x] = c
print("".join(T))
