n, q = map(int, input().split())

front = [-1] * (n + 1)
back = [-1] * (n + 1)

for _ in range(q):
    nums = list(map(int, input().split()))

    if nums[0] == 1:
        x, y = nums[1], nums[2]
        back[x] = y
        front[y] = x
    if nums[0] == 2:
        x, y = nums[1], nums[2]
        back[x] = -1
        front[y] = -1
    if nums[0] == 3:
        x = nums[1]
        while front[x] != -1:
            x = front[x]

        ret = []
        while x != -1:
            ret.append(x)
            x = back[x]

        print(len(ret), *ret)
