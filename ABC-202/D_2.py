a, b, k = map(int, input().split())

now = 0
ans = ""


def perm(_a: int, _b: int) -> int:
    ret = 1
    for i in range(1, _a + 1):
        ret *= _b + i
        ret //= i
    return ret


while a + b > 0:
    if a == 0:
        ans += "b"
        b -= 1
        continue
    elif b == 0:
        ans += "a"
        a -= 1
        continue

    next: int = perm(a - 1, b)
    if now + next < k:
        b -= 1
        now += next
        ans += "b"
        continue
    elif now + next >= k:
        a -= 1
        ans += "a"


print(ans)
