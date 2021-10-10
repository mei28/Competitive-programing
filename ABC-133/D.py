n = int(input())
A = list(map(int, input().split()))

A = list(map(lambda x: x * 2, A))

# x0 = 0のとき
offset = 0
for i in range(n):
    offset = A[i] - offset

x = offset / 2

cur = x
for i in range(n):
    print(int(cur))
    cur = A[i] - cur
