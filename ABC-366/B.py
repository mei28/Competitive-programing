n = int(input())
S = [input() for _ in range(n)]

max_len = max([len(s) for s in S])


for i in range(max_len):
    ans = ""
    for j in range(n):
        if i < len(S[j]):
            ans = S[j][i] + ans
        else:
            ans = "*" + ans

    ans = ans.rstrip("*")
    print(ans)
