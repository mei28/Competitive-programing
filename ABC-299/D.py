N = int(input())

if N == 2:
    print("!", 1)
    exit()

l = 0
r = N
dic = dict()
dic[0] = 0
dic[1] = 1
while 1:
    mid = (l + r) // 2
    print("?", mid + 1)
    S = int(input())
    dic[mid] = S
    if mid + 1 in dic and dic[mid] != dic[mid + 1]:
        print("!", mid + 1)
        break
    if S:
        r = mid
    else:
        l = mid
