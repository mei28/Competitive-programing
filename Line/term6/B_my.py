import re
import sys


class Levenshtein:
    def __init__(self, str1: str, str2: str) -> None:
        self.str1 = str1
        self.str2 = str2
        self.dp = self.initDP(str1, str2)
        self.dist = self.editDist(str1, str2, self.dp)

    # dpテーブルの初期化
    def initDP(self, str1: str, str2: str):
        dp = []
        for i in range(len(str1) + 1):
            dp.append([0] * (len(str2) + 1))
            dp[i][0] = i
        for j in range(len(str2) + 1):
            dp[0][j] = j
        return dp

    # 編集距離の更新
    def editDist(self, str1: str, str2: str, dp) -> int:
        # dist[挿入,削除,置換]
        dist = [0] * 3
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                dist[0] = (
                    dp[i - 1][j - 1]
                    if str1[i - 1] == str2[j - 1]
                    else dp[i - 1][j - 1] + 1
                )
                dist[1] = dp[i][j - 1] + 1
                dist[2] = dp[i - 1][j] + 1
                dp[i][j] = min(dist)
        return dp[i][j]


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
    if not len(lines) == 2:
        if len(lines) == 0:
            print(0)
            exit()
        elif len(lines) == 1:
            print(len(lines[0]))
            exit()
        elif len(lines) >= 3:
            # 仕様に違反する場合
            sys.exit(100)
    else:
        s = lines[0]
        t = lines[1]
        check = check_input(s, t)
        if check:
            print(Levenshtein(s, t).dist)
        else:
            # 仕様に違反している
            sys.exit(100)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
