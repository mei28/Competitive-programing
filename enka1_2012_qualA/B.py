S = input()

n = len(S)

idx = 0
ans = ""

while idx < n:
    if S[idx] != " ":
        ans += S[idx]
        idx += 1
    else:
        ans += ","
        while idx < n and S[idx] == " ":
            idx += 1

print(ans)
