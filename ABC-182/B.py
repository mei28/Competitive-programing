N = int(input())
A = list(map(int, input().split()))

max_ = max(A)
ans = 2
max_cnt = 0
for i in range(2, max_+1):
    tmp_cnt = 0
    for a in A:
        if a % i == 0 and a >= i:
            tmp_cnt += 1
    if max_cnt <= tmp_cnt:
        max_cnt = tmp_cnt
        ans = i

print(ans)
