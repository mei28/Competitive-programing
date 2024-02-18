S = input()


a = [0] * (len(S) + 1)

for i, s in enumerate(S):
    if s == "<":
        a[i + 1] = a[i] + 1

n = len(S)

for i in range(n - 1, -1, -1):
    if S[i] == ">":
        if a[i] <= a[i + 1]:
            a[i] = a[i + 1] + 1

print(sum(a))
