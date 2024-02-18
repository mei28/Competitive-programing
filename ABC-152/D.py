n = int(input())

# cnt[i][j] : 先頭がi，末尾がjである個数

cnt = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    head = int(str(i)[0])
    tail = int(str(i)[-1])

    cnt[head][tail] += 1


ans = 0

for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
