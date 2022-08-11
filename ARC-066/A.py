from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A.sort()

MOD = 1000000007

cnt = Counter(A)

if n % 2 == 1:
    if cnt[0] != 1:
        print(0)
        exit()
    for i in range(2, n, 2):
        if cnt[i] != 2:
            print(0)
            exit()

else:
    for i in range(1, n, 2):
        if cnt[i] != 2:
            print(0)
            exit()

print(pow(2, n // 2, MOD))
