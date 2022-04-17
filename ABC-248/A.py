S = list(input())
S.sort()

for i in range(10):
    if not str(i) in S:
        print(str(i))
        exit()
