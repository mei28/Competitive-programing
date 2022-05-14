n = int(input())
ST = []
S = []
T = []


one_k = set()
for i in range(n):
    s, t = input().split()
    t = int(t)
    if s in one_k:
        continue
    one_k.add(s)
    ST.append([s, t, i + 1])
    T.append(t)
    S.append(s)

ST = list(sorted(ST, key=lambda x: (x[1]), reverse=True))
for tmp in ST:
    s, t, i = tmp
    print(i)
    exit()
