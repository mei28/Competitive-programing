n = int(input())
s = input()

cnt = 0
left_cnt = 0
right_cnt = 0

for i in s:
    if i == "(":
        cnt += 1
    elif i == ")":
        if cnt <= 0:
            left_cnt += 1
        else:
            cnt -= 1

print("(" * left_cnt + s + ")" * cnt)
