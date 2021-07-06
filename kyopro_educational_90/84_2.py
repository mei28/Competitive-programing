n = int(input())
s = input()
A = [0] * (1 << 20)
B = [0] * (1 << 20)

for i in range(1, n + 1):
    if s[i - 1] == "o":
        A[i] = i
        B[i] = B[i - 1]
    else:
        B[i] = i
        A[i] = A[i - 1]

ans = 0

for i in range(1, n + 1):
    ans += min(A[i], B[i])

print(ans)
