T = int(input())


def solve_13(n1: int, n3: int):
    ans = 0
    k = min(n1 // 2, n3)

    n1 -= 2 * k
    n3 -= k
    ans += k

    ans += n1 // 5
    return ans


def solve(n2: int, n3: int, n4: int):
    n1, n2, n3 = n2, n4, n3 // 2
    ans: int = 0

    k = min(n2, n3)
    n2 -= k
    n3 -= k

    ans += k

    if n2 == 0:
        ans += solve_13(n1, n3)
    return ans


for _ in range(T):
    n2, n3, n4 = map(int, input().split())
    print(solve(n2, n3, n4))
