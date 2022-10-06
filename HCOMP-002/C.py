from collections import deque

S = input()
stack = deque()

cnt = 0
last = ""

for s in S:
    if len(stack) == 0:
        stack.append(s)
        last = s
    else:
        if s != last:
            stack.pop()
            cnt += 2
            if len(stack) == 0:
                last = ""
            else:
                last = stack.pop()
                stack.append(last)
        else:
            stack.append(s)
            last = s
print(cnt)
