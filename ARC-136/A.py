n = int(input())
S = input()

ans = ""
i = 0
while i < n:
    if S[i] == "C":
        ans += S[i]
        i += 1
    else:
        j = i
        cnt = 0

        while j < n and S[j] != "C":
            if S[j] == "A":
                cnt += 2
            else:
                cnt += 1
            j += 1

        ans += "A" * (cnt // 2)
        if cnt % 2 == 1:
            ans += "B"
        i = j
print(ans)
