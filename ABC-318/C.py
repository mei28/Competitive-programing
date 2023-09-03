N, D, P = map(int, input().split())
F = list(map(int, input().split()))
# 運賃を昇順にソート
F.sort(reverse=True)

# コストの合計を初期化
total_cost = 0

i = 0
while i < N:
    if sum(F[i : min(i + D, N)]) > P:
        total_cost += P
        i += D
    else:
        total_cost += sum(F[i:N])
        break

print(total_cost)
