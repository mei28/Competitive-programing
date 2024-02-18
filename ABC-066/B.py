S = input()

N = len(S)

ans = 0
for i in range(2, N + 1, 2):
    j = i // 2
    left = S[:j]
    right = S[j:i]
    if left == right and i < N:
        ans = i

print(ans)
