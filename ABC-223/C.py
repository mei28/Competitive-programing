import bisect

n = int(input())

A, B = [], []
T = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(a / b)

if n == 1:
    print(A[0] / 2)
    exit()

all_time = sum(T)
col_time = all_time / 2

sum_time = [0] * (n + 1)

for i in range(n):
    sum_time[i + 1] = sum_time[i] + T[i]
del sum_time[0]


def bi(l: list, a: float):
    ok = 0
    ng = n
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if l[mid] <= a:
            ok = mid
        else:
            ng = mid
    return ok


col_idx = bi(sum_time, col_time)


ans = 0
for i in range(col_idx + 1):
    ans += A[i]

ans += B[col_idx + 1] * (col_time - sum_time[col_idx])
print(ans)
