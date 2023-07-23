n, d = map(int, input().split())
S = [input() for _ in range(n)]

T = [0] * d

for s in S:
    for i in range(d):
        if s[i] == "o":
            T[i] += 1


def rle(s):
    n = len(s)  # 文字列の長さ
    ans = []  # 圧縮後のリスト
    l = 0  # 始点
    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:  # 異なる文字になるまで進む
            r += 1
        ans.append((s[l], r - l))  # 文字,連続する個数
        l = r  # 連続しなかった文字から探索を開始
    return ans


ret = rle([str(t) for t in T])
ans = 0
for i, t in ret:
    if int(i) == n:
        ans = max(ans, t)
print(ans)
