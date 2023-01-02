n, k = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0


ans = 0


def is_ng(l, r):
    if A[r] - A[l] > k:
        return True
    else:
        return False


def check(l, r):
    global ans
    r = min(r, n - 1)
    l = min(l, n - 1)
    if A[r] - A[l] <= k:
        ans += 1


while left < n:
    if right == n or is_ng(left, right):
        left += 1
    else:
        right += 1

    check(left, right)
print(ans)
