import sys

import sys
import re

from leven import levenshtein


def isAlNum(s: str) -> bool:
    pat = re.compile(r'^[A-Za-z0-9]+$')
    return pat.match(s) is not None


def check_input(s: str, t: str) -> bool:
    if isAlNum(s) and isAlNum(t):
        # 英数文字のとき
        return True
    return False


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    lines = lines[0].split()
    # 2つ入力あるか?
    if len(lines) == 0:
        s = 'a'
        t = 'a'
    elif len(lines) == 1:
        s = lines[0]
        # sの先頭とは違う文字にする
        t = chr((ord(s[0])+1) % 25 + 48)
    elif len(lines) == 2:
        s = lines[0]
        t = lines[1]
    elif len(lines) >= 3:
        sys.exit(100)

    check = check_input(s, t)

    if check:
        print(levenshtein(s, t))
    else:
        sys.exit(100)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。
#     # ---
#     # This is a sample code to use stdin and stdout.
#     # Edit and remove this code as you like.

#     lines = lines[0].split()
#     s = lines[0]
#     t = lines[1]

#     MY_INF = 1 << 29

#     dp = [[MY_INF for _ in range(len(s)+1)] for _ in range(len(t)+1)]

#     dp[0][0] = 0
#     for i in range(len(s)+1):
#         for j in range(len(t)+1):

#             # 変更のとき
#             if i > 0 and j > 0:
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = min(dp[i][j], dp[i-1][j-1])
#                 else:
#                     dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)

#             # 削除の時
#             if i > 0:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j]+1)

#             # 挿入の時
#             if j > 0:
#                 dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

#     print(dp[-1][-1])


# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)
