def find(x):
    if par[x] < 0:
        return x

    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x


def same(x, y):
    return find(x) == find(y)


n = int(input())
names = set()
S, T = [], []
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

par = [-1] * len(names)


for s, t in zip(S, T):
    ss = str2num[s]
    tt = str2num[t]
    if same(ss, tt):
        print("No")
        exit()
    union(ss, tt)
print("Yes")
