from os import name


n = int(input().split())

names = set()
S, T = [], []
for _ in range(n):
    s, t = map(int, input().split())
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
