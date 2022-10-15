x, k = map(int, input().split())
s = str(x)
n = len(s)
r = s[::-1]
ans = ""
if n < k:
    print(0)
    exit()

inc = 0
for i in range(k):
    tmp = int(s[-(i + 1)]) + inc
    if tmp >= 5:
        inc = 1
    else:
        inc = 0

S = [*s]

if n == k:
    S.insert(0, "0")
    if int(S[-(k + 1)]) + inc <= 9:
        S[-(k + 1)] = str(int(S[-(k + 1)]) + inc)
        for i in range(k):
            S[-(i + 1)] = "0"
    if len(set(S)) == 1:
        print(0)
    else:
        print("".join(S))
else:
    if int(S[-(k + 1)]) + inc <= 9:
        S[-(k + 1)] = str(int(S[-(k + 1)]) + inc)
        for i in range(k):
            S[-(i + 1)] = "0"
    print("".join(S))
