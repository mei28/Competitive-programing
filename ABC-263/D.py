n, l, r = map(int, input().split())
A = list(map(int, input().split()))

accumulate = [0]

for ele in A:
    accumulate.append(accumulate[-1] + ele)

ans = l * n
for left in range(n + 1):
    for right in range(l, n + 1):
        tmp = left * l + (n - right) * r + (accumulate[right] - accumulate[left])
        ans = min(ans, tmp)
