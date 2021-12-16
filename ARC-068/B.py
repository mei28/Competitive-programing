n = int(input())
A = list(map(int,input().split()))

ans = len(set(A))

if not ans % 2:
    ans -=1

print(ans)
