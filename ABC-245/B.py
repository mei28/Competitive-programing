n = int(input())
A = list(map(int,input().split()))

i = 0

while True:
    if i not in A:
        print(i)
        exit()
    i+=1
