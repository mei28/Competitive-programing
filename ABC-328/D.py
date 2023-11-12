from collections import deque


def remove_abc_substring_optimized(s):
    s_deque = deque()
    for char in s:
        s_deque.append(char)
        if (
            len(s_deque) >= 3
            and s_deque[-1] == "C"
            and s_deque[-2] == "B"
            and s_deque[-3] == "A"
        ):
            s_deque.pop()
            s_deque.pop()
            s_deque.pop()
    return "".join(s_deque)


s = input()
print(remove_abc_substring_optimized(s))
