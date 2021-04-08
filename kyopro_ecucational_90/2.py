N = int(input())
if N % 2 == 1:
    print()
    exit()


def check(s: str) -> bool:
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        elif cnt > 0 and i == ")":
            cnt -= 1
        else:
            return False
    if cnt > 0:
        return False
    return True


ans = set()

for bit in range(2 << N):
    tmp = ""
    for j in range(N):
        if (bit >> j) % 2 == 1:
            tmp += "("
        else:
            tmp += ")"
    if check(tmp):
        ans.add(tmp)

for i in ans:
    print(i)
