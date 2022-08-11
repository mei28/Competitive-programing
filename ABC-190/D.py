n = int(input())

# 初項a, である一般はa_n = a + n
# S_n = n(2a+n-1)/2
# つまり，2N = n(2a+n-1)
# となるようなa,nの個数を求めればよい
#  nは2Nの正の約数となる必要がある
# m = 2N/n とすると m-n = 2a-1 となるから, m-nが奇数となる -> m-nが奇数ならば，aが一意に決まる
# つまり，2Nの約数dであり，dと2N/dの偶奇がことなるものの個数を求める


def div(m: int) -> set:
    res = set()

    i = 1
    while i * i <= m:
        if m % i == 0:
            res.add(i)
            res.add(m // i)

        i += 1
    return res


D = div(2 * n)

ans = 0
for d in D:
    m = (2 * n) // d
    if (d - m) % 2 == 1:
        ans += 1

print(ans)
