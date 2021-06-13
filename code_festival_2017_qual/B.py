n, m, k = map(int, input().split())
# p行列とq行列が反転している時，黒になっている個数を求める
# (M-q) * p + (N-p)*q


for p in range(n + 1):
    for q in range(m + 1):
        if (m - q) * p + (n - p) * q == k:
            print("Yes")
            exit()

print("No")
