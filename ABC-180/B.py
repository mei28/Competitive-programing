import math 
N = int(input())
X = list(map(int, input().split()))

a=0
b=0 
c=[]

for x in X:
    a += abs(x)
    b += abs(x)**2
    c.append(abs(x))

print(a)
print(math.sqrt(b))
print(max(c))
