def Base_10_to_n(X, n=8):
    if int(X / n):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


N = int(input())

cnt = 0
for i in range(1, N + 1):
    oc = Base_10_to_n(i, 8)
    if "7" in oc or "7" in str(i):
        cnt += 1
print(N - cnt)
