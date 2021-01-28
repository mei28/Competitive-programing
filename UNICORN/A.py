import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    lines = lines[0].split()
    num = int(lines.pop(-1))
    dct = {}
    for l in lines:
        k, v = l.split(':')
        k = int(k)
        dct[k] = v
    # sort
    sorted_dct = {}
    for k, v in sorted(dct.items()):
        sorted_dct[k] = v
    dct = sorted_dct

    flg = True
    for k, v in dct.items():
        if num % k == 0:
            print(v, end='')
            flg = False
    if flg:
        print(num)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
