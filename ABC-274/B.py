h, w = map(int, input().split())
C = [input() for _ in range(h)]

ans = []
for i in range(w):
    cnt = 0
    for j in range(h):
        if C[j][i] == "#":
            cnt += 1
    ans.append(cnt)
print(*ans)
