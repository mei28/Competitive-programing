n = bin(int(input()))[2:]
m = n[::-1]

ans = list()


def dfs(a: str, i: int):
    if len(a) == len(m):
        ans.append(a[::-1])
        return
    if m[i] == "1":
        for j in ["0", "1"]:
            a += j
            dfs(a, i + 1)
            a = a[:-1]
    else:
        a += "0"
        dfs(a, i + 1)
        a = a[:-1]


dfs("", 0)
ans.sort()
for a in ans:
    print(int(a, 2))
