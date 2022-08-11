import sys
import queue


def make_menu(M: int) -> dict:
    Menu = {}
    # 初期情報を追加
    for i in range(M):
        tmp = list(lines[0].split())
        D, S, P = tmp[0], int(tmp[1]), int(tmp[2])
        Menu[D] = [S, P]
        lines.pop(0)
    return Menu


def check_zaiko(zaiko: int, n_tyumon: int) -> bool:
    if zaiko >= n_tyumon:
        return True
    else:
        return False


def update_zaiko(M: dict, D: str, N: int) -> dict:
    M[D][0] -= N
    return M


def show_order_result(T: str, D: str, N: int, ok=True):
    if ok:
        for i in range(N):
            print(f"received order {T} {D}")
    else:
        for i in range(1):
            print(f"sold out {T}")


def get_order(Menu: dict, order: list):
    T, D, N = order[0], order[1], int(order[2])
    if check_zaiko(Menu[D][0], N):
        Menu = update_zaiko(Menu, D, N)
        show_order_result(T, D, N, ok=True)
    else:
        show_order_result(T, D, N, ok=False)

    return Menu


def do_step1():
    M = int(lines.pop(0))
    # D:[S,P]
    Menu = {}
    # 初期情報を追加
    for i in range(M):
        tmp = list(lines[0].split())
        D, S, P = tmp[0], int(tmp[1]), int(tmp[2])
        Menu[D] = [S, P]
        lines.pop(0)

    # オーダを受け取る
    for l in lines:
        task, T, D, N = l.split()
        order = [T, D, N]
        Menu = get_order(Menu, order)


def do_step2():
    M, K = map(int, lines.pop(0).split())
    # Menu D:[S,P]
    Menu = make_menu(M)

    order_queue = queue.Queue()
    # oven
    oven = []

    for l in lines:
        if len(l.split()) == 4:
            # オーダを受け取る時 received order T D
            tmp = list(l.split())
            T, D = tmp[2], tmp[3]
            # 注文リストに追加
            if len(oven) < K:
                # オーブンにあきがある
                print(D)
                oven.append(D)
            else:
                # オーブンにあきがない
                order_queue.put([T, D])
                print("wait")

        else:
            # 完成する時
            _, D = l.split()
            if D not in oven:
                # そうでない場合
                print("unexpected input")
            else:
                # オーブンから外す
                oven.remove(D)
                if order_queue.empty():
                    print("ok")
                else:
                    order = order_queue.get()
                    oven.append(order[1])
                    print("ok {}".format(order[1]))


def do_step3():
    M = int(lines.pop(0))

    # Menu D:[S,P]
    Menu = make_menu(M)
    # key: D, val: [T_1,...]
    order_dict = dict()
    if l in lines:
        if len(l) == 4:
            # 注文を受け取るとき
            tmp = list(l.split())
            T, D = tmp[2], tmp[3]
            order_list[D] = order_list.setdefault(D, []) + [T]
        else:
            _, D = list(l.split())
            tmp = order_dict[D].pop(0)
            print(f"ready {tmp} {T}")


def main(lines):
    step = lines.pop(0)
    if step == "1":
        do_step1()

    elif step == "2":
        do_step2()

    elif step == "3":
        do_step3()


if __name__ == "__main__":
    lines = []
    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))

    for i in range(9):
        lines.append(input())
    main(lines)
