n, k = map(int, input().split())
S = input()

a = 0
for i in range(n - 1):
    if S[i] != S[i + 1]:
        a += 1

print(n - 1 - max(a - k * 2, 0))
