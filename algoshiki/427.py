n, x = map(int, input().split())
A = list(map(int, input().split()))


def f(i, j):
    if i == 0:
        if j == 0:
            return True
        else:
            return False
    if not i == 0:
        flg = False
        if j >= A[i - 1] and f(i - 1, j - A[i - 1]):
            flg = True
        elif f(i - 1, j):
            flg = True
        return flg


print("Yes") if f(n, x) else print("No")
