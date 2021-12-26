x, y = map(int,input().split())

if x>=y:
    print(0)
    exit()

y -= x
print(-(-y//10))
