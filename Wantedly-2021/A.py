# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y):
    # write your code in Python 3.6
    n = len(X)
    ans = 0
    for i in range(1, n):
        h = X[i] - X[i - 1]
        ans += h * (Y[i] + Y[i - 1]) / 2
    return ans
