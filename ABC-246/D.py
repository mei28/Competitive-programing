n = int(input())

def f(a,b):
    return a**3 + (a**2) * b + (b**2)*a + b**3

x = -1

j = 10**6

for i in range(10**6):
    while f(i,j) >=n and j>=0:
        if x==-1:
            x = f(i,j)
        x = min(f(i,j),x)
        j-=1

print(x)
