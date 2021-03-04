# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import sys


def solution(S):
    # write your code in Python 3.6
    st = stack(len(S)+1000)
    S = S.split(' ')
    for s in S:
        if str(s).isdecimal():
            st.push(s)
        else:
            try:
                if s == 'POP':
                    st.pop()
                elif s == 'DUP':
                    b = st.pop()
                    st.push(b)
                    st.push(b)
                elif s == '+':
                    b = int(st.pop())
                    a = int(st.pop())
                    st.push(str(b+a))
                elif s == '-':
                    b = int(st.pop())
                    a = int(st.pop())
                    st.push(str(b-a))
            except Exception:
                return -1
    return int(st.pop())


class stack:
    def __init__(self, MAX=10):
        self.MAX = MAX
        self.s = []

    def __isEmpty__(self):
        return len(self.s) == 0

    def __isFull__(self):
        return len(self.s) >= self.MAX-1

    def push(self, x):
        if self.__isFull__():
            # sys.exit('overflow!')
            raise Exception

        self.s.append(x)

    def pop(self):
        if self.__isEmpty__():
            raise Exception
            # sys.exit('underflow!')
        return self.s.pop()
