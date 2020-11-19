N = int(input())

A = [-1 for i in range(N + 1)]

for i in range(1, N + 1):
    A[i] = int(input())


i = 0
now = 1
while True:
    if i > N + 3:
        print(-1)
        exit()
    if now == 2:
        print(i)
        exit()
    now = A[now]
    i += 1
