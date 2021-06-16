def base8to10(s: str) -> int:
    ans: int = 0
    x: int = 1
    m: int = len(s)

    for i in range(m - 1, -1, -1):
        ans += int(s[i]) * x
        x *= 8
    return ans


def base10to9(s: int) -> str:
    ans: str = ""
    if s == 0:
        return "0"
    while s > 0:
        c = str(s % 9)
        ans = c + ans
        s //= 9
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    for _ in range(k):
        tmp: int = base8to10(str(n))
        tmp: str = base10to9(tmp)
        tmp: str = tmp.replace("8", "5")
        n = tmp

    print(n)
