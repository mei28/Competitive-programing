N = int(input())
S = input()

max_cnt = 0
now_cnt = 0
for i in S:
    if i == 'I':
        now_cnt += 1
    else:
        now_cnt -= 1
    max_cnt = max(max_cnt, now_cnt)

print(max_cnt)