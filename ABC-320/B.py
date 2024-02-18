S = input()
n = len(S)

ans = 1
for i in range(n):
    for j in range(n):
        a = S[i : i + j + 1]
        b = S[i : i + j + 1][::-1]
        if a == b:
            ans = max(ans, len(a))
print(ans)
