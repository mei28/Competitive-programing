n = int(input())
SA = [list(input().split()) for _ in range(n)]

min_A = 10**9
min_A_index = 0

for i, (s, a) in enumerate(SA):
    if min_A > int(a):
        min_A = int(a)
        min_A_index = i

for i in range(n):
    print(SA[(i + min_A_index) % n][0])
