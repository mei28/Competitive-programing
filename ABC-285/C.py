import string

S = input()
S = S[::-1]

ALP = string.ascii_uppercase

ans = 0

for i, s in enumerate(S):
    ans += 26**i * (ALP.index(s) + 1)
print(ans)
