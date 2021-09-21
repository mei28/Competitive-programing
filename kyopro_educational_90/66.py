n = int(input())

all_ = 1
sum_ = 0

pre_l = 0
pre_r = 0
for i in range(n):
    l, r = map(int, input().split())
    all_ *= r - l + 1
    if i == 0:
        pre_r = r
        pre_l = l
        continue

print(sum_, all_)


print(sum_ / all_)
