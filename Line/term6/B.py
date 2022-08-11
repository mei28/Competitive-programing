import re
import sys

from leven import levenshtein


def isAlNum(s: str) -> bool:
    # アルファベット，数字かどうか
    pat = re.compile(r"^[A-Za-z0-9]+$")
    return pat.match(s) is not None


def check_input(s: str, t: str) -> bool:
    if isAlNum(s) and isAlNum(t):
        # 英数文字のときTrue
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
        s = "a"
        t = "a"
    elif len(lines) == 1:
        s = lines[0]
        # sの先頭とは違う文字にする
        t = chr((ord(s[0]) + 1) % 25 + 48)
    elif len(lines) == 2:
        s = lines[0]
        t = lines[1]
    elif len(lines) >= 3:
        # 仕様に違反する場合
        sys.exit(100)

    check = check_input(s, t)

    if check:
        print(levenshtein(s, t))
    else:
        # 仕様に違反している
        sys.exit(100)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
