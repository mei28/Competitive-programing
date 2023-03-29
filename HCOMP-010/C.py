S = input()

n = len(S)

ans = n * (n - 1)

for i, s in enumerate(S):
    if s == "U":
        ans += i
    else:
        ans += n - i - 1
print(ans)
