import sys

sys.setrecursionlimit(10**5)
n = int(input())
S, T = [], []
names = set()
for _ in range(n):
    s, t = input().split()
    S.append(s)
    T.append(t)
    names.add(s)
    names.add(t)

str2num: dict = {}
num2str: dict = {}

for i, name in enumerate(names):
    str2num[name] = i
    num2str[i] = name


G = [[] for _ in range(len(names))]

for s, t in zip(S, T):
    ss = str2num[s]
    tt = str2num[t]
    G[ss].append(tt)
    G[tt].append(ss)


def dfs(v, last=-1):
    global visited
    if last != -1:
        parents[v] = last
    visited[v] = True

    for nv in G[v]:
        if nv == last:
            continue
        if visited[nv]:
            return True
        else:
            if dfs(nv, v):
                return True
    return False


n = len(names)
for i in range(n):
    parents = [-1] * n
    loop = set()
    visited = [False] * n
    if dfs(i):
        print("No")
        exit()
print("Yes")
