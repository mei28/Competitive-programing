import sys


def check_set(s: str) -> bool:
    _s = set(s)
    symbol_set = set(["@", "$", "%"])
    _s_alp = _s - symbol_set
    _s_symbol = _s & symbol_set
    if len(_s_alp) >= 5 and _s_symbol:
        return True
    else:
        return False


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    s = lines[0]

    for i in range(6, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            _tmp = s[j : j + i]
            if check_set(_tmp):
                print(len(_tmp))
                exit()


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
