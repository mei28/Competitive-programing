N = int(input())
A = map(int,input().split())

k1, k2, k4 = 0,0,0 

for a in A:
    if a%4==0:
        k4+=1
    elif a % 2==0:
        k2+=1
    else:
        k1+=1

t = min(k1,k4)
k1 -= t
k4 -= t

result = k1 ==0 or (k1==1 and not k2)

print(['No','Yes'][result])
