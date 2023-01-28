from bisect import bisect_left

q = int(input())
S = set()


for _ in range(q):
    l = input().split()
    x = int(l[1])
    if l[0] == "1":
        S.add(x)
    elif l[0] == "2":
        S.remove(x)
    elif l[0] == "3":
        T = sorted(list(S))
        idx = bisect_left(T, x)
        if idx == len(T):
            print(-1)
        else:
            print(T[idx])
