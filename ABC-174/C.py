k = int(input())

A = [-1]*(k+10)

A[1]= 7%k

for i in range(2,k+2):
    A[i] = (A[i-1]*10+7)%k

for i in range(1,k+3):
    if A[i]==0:
        print(i)
        exit()

print(-1)
