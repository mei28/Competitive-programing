S = list(input())
A = ""
for i in range(0, len(S), 2):
    A += S[i + 1] + S[i]
print(A)
