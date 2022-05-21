from collections import Counter

n = int(input())
A = list(map(int, input().split()))

cnter = Counter(A)
A.sort()
keys = cnter.keys()

ans = 0

B = []
for k, v in cnter.items():
    B.append(v)
S = [0] * (len(B) + 1)
for i in range(len(B)):
    S[i + 1] = S[i] + B[i]

    # print(B)
    # print(S)
for j in range(1, len(B) - 1):
    ans += (S[j] - S[0]) * B[j] * (S[-1] - S[j + 1])
    # print(i, j, ans, B[i], B[j], S[-1] - S[j])

print(ans)
