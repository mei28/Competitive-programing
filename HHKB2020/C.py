N = int(input())
P = map(int,input().split())

min_bool = [False for _ in range(200100)]

min_idx = 0
for i in P:
    min_bool[i] = True
    for i in range(min_idx,len(min_bool)):
        if min_bool[i] == False:
            min_idx = i
            print(min_idx)
            break