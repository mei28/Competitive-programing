from collections import deque

n = int(input())
S = input()
T = input()

if sorted(S) != sorted(T):
    print("No")
    exit()


def check(k):
    right = deque(S[k:])
    for t in T:
        if right[0] == t:
            right.popleft()
        if len(right) == 0:
            return True
    return False


ng = -1
ok = n

while ok - ng > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
