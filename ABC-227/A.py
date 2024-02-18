n, k, a = map(int, input().split())
k -= n - a + 1

a = k % n
if a == 0:
    print(n)
else:
    print(a)
