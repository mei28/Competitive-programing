import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N = int(lines[0])
    line = lines[1]
    line = list(map(int, line.split()))
    # sort
    line.sort()
    # cut
    line = line[1:-1]
    # calc mean
    print(sum(line)/len(line))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
