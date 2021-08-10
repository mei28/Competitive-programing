# 数字nを入力として受け取る
n = int(input())

# 数字のリストを受け取る
nums = list(map(int, input().split()))
N = []
for i, e in enumerate(nums):
    N.append((e, i + 1))

N.sort()
print(N[-2][1])
