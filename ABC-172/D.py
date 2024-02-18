N = int(input())

# 約数の個数を数え上げる
# O(nlogn)
div = [0] * (N + 1)
for n in range(1, N + 1):
    for m in range(n, N + 1, n):
        div[m] += 1

ans = 0
for i in range(1, n + 1):
    ans += i * div[i]

print(ans)
