s = input()
ss = s + s

S = set()
for i in range(len(s)):
    tmp = ss[i : i + len(s)]
    S.add(tmp)

S = list(S)
S.sort()
print(S[0])
print(S[-1])
