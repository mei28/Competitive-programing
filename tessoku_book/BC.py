q = int(input())
S = set()


def lower_bound(x, A):
    ng = -1
    ok = len(A)
    while ok - ng > 1:
        mid = ok + ng
        if x <= A[mid]:
            ok = mid
        else:
            ng = mid
    return ok


for _ in range(q):
    l = input().split()
    x = int(l[1])
    if l[0] == "1":
        S.add(x)
    elif l[0] == "2":
        S.remove(x)
    elif l[0] == "3":
        T = sorted(list(S))
        idx = lower_bound(x, T)
        if idx == len(T):
            print(-1)
        else:
            print(T[idx])
