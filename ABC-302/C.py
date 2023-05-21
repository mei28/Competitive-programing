from itertools import permutations

n, m = map(int, input().split())
S = [input() for _ in range(n)]

perms = list(permutations(range(n), n))

for perm in perms:
    tmp = []
    for i in perm:
        tmp.append(S[i])
    flg = True
    for j in range(1, n):
        left = tmp[j - 1]
        right = tmp[j]

        cnt = sum([a != b for a, b in zip(left, right)])
        if cnt > 1:
            flg = False
            break
    if flg:
        print("Yes")
        exit()
print("No")
