S = [i for i in input()]
k = int(input())

for i in range(len(S)):
    condition = ((ord("a") - ord(S[i])) + 26) % 26

    if condition <= k:
        S[i] = "a"
        k -= condition

    if i == len(S) - 1:
        k %= 26
        S[i] = chr(ord(S[i]) + k)

print("".join(S))
