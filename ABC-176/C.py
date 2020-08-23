N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    front = A[i - 1]
    back = A[i]

    if front > back:
        diff = front-back 
        cnt += diff
        A[i] = A[i] + diff

    # print(A)
print(cnt)