N = int(input())
b = list(map(int, input().split()))

ans = []

for i in range(N - 1, -1, -1):
    flg = False
    for j in range(i, -1, -1):
        if b[j] == j + 1:
            ans.append(b[j])
            del b[j]
            flg = True
            break

    if not flg:
        print(-1)
        exit()

ans.reverse()
print(*ans)
