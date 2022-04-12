from collections import deque


def main():
    Q = int(input())
    deq = deque()
    for _ in range(Q):
        q, *_a = map(int, input().split())
        if q == 1:
            x, c = _a
            deq.append([x, c])  # xが書かれたボールを右からc個入れる
        else:
            c = _a[0]  # cが0になるまでボールを取り出し続けます
            sm = 0  # 取り出したボールに書かれた数の合計
            while c > 0:
                num, cnt = deq[0]
                if c >= cnt:
                    sm += num * cnt
                    deq.popleft()  # この塊のボールを全部取り出したので、deqから削除します
                    c -= cnt
                else:
                    sm += num * c
                    deq[0][1] -= c  # cntではなく、deq[0][1] を c個減らしてください（cntは、deq[0][1]の値をコピーした別の実体です）
                    c = 0
            print(sm)  # 忘れずに


if __name__ == '__main__':
    main()

