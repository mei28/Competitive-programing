n, m = map(int, input().split())


def calc_divisor(n: int) -> list:
    ans: list = [1]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            j = n // i
            if j != i:
                ans.append(j)
    ans.sort()
    return ans


ans = 1
for i in calc_divisor(m):
    if i * n <= m:
        ans = i
print(ans)
