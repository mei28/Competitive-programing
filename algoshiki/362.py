n = int(input())
ans = 0

while n>0:
    if n%2==0:
        n//=2
    else:
        n-=1
    ans +=1

print(ans)
