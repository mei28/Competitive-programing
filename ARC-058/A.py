n,k = map(int,input().split())
D = list(map(int,input().split()))

def is_valid(x:int)->bool:
    while x:
        if x%10 in D:
            return False
        x//=10

    return True

for i in range(n,n*n+10):
    if is_valid(i):
        print(i)
        exit()
