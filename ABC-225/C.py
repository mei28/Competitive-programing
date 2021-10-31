n, m = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(n)]


def check(s):
    pre = s[0]
    pre_a = (s[0] - 1) % 7
    for i in range(1, len(s)):
        if s[i] - pre != 1:
            return False
        if pre_a > (s[i] - 1) % 7:
            return False
        pre = s[i]
        pre_a = (s[i] - 1) % 7
    return True


flg = True
for i in range(n):
    for j in range(m):
        flg = check(B[i])
        if not flg:
            print("No")
            exit()

pre = B[0][0]
for i in range(1, n):
    tmp = B[i][0]
    if tmp - pre != 7:
        print("No")
        exit()
    pre = tmp

print("Yes")
