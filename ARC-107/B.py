n, k = map(int, input().split())
# =====================
# a+b - (c+d) = k -> a+b = k+c+d
# k + 2 <= a+b <= 2*n
# X = K + Y := X=a+b, Y=c+d
# 2<= X <= N+1
# (a,b) = (1,X-1),,,(X-1,1) => n-1
# N+2<=X<=2*N
# (a,b) = (N,X-N),,,(X-N,N) => 2N-X+1
# =====================


def f(x: int) -> int:
    if x >= n + 2:
        return n - (x - n) + 1
    else:
        return x - 1


k: int = abs(k)

ans: int = 0

for i in range(k + 2, 2 * n + 1):
    ans += f(i) * f(i - k)

print(ans)
