def do_step1(step, n, m, q, query1, query2, query3):
    cnt = [{} for _ in range(n + 1)]
    ret = []
    for x, y, z in zip(query1, query2, query3):
        if z != -1:
            cnt[x][y] = cnt[x].setdefault(y, 0) + z
        else:
            a, b = x, y
            ans = 0
            for i in range(1, n + 1):
                sum_ = sum(cnt[i].values())
                val = cnt[i].get(a, 0)
                if sum_ == 0:
                    continue
                if val / sum_ * 100 >= b:
                    ans += 1
            ret.append(ans)

    return ret


def do_step2(step, n, m, q, query1, query2, query3):
    cnt = {}
    ret = []

    for x, y, z in zip(query1, query2, query3):
        if z != -1:
            if x not in cnt:
                cnt[x] = {"sum": 0, "values": {}}

            cnt[x]["sum"] += z - cnt[x]["values"].get(y, 0)
            cnt[x]["values"][y] = cnt[x]["values"].setdefault(y, 0) + z
        else:
            a, b = x, y
            ans = 0
            for i in cnt:
                total = cnt[i]["sum"]
                val = cnt[i]["values"].get(a, 0)
                if total > 0 and val / total * 100 >= b:
                    ans += 1
            ret.append(ans)
    return ret


def do_step3(step, n, m, q, query1, query2, query3):
    cnt = {}
    # キャッシュ用のディクショナリを追加
    cache = {}
    ret = []

    for x, y, z in zip(query1, query2, query3):
        if z != -1:
            # 値の更新
            if x not in cnt:
                cnt[x] = {"sum": 0, "values": {}}
            prev_value = cnt[x]["values"].get(y, 0)
            cnt[x]["sum"] += z - prev_value
            cnt[x]["values"][y] = prev_value + z
        else:
            # キャッシュのチェック
            if (x, y) in cache:
                # キャッシュから結果を取得
                ret.append(cache[(x, y)])
                continue

            # クエリの処理
            a, b = x, y
            ans = 0
            for i in cnt:
                total = cnt[i]["sum"]
                val = cnt[i]["values"].get(a, 0)
                if total > 0 and val / total * 100 >= b:
                    ans += 1

            # 結果をキャッシュ
            cache[(x, y)] = ans
            ret.append(ans)

    return ret


def create_solution(
    step: int,
    n: int,
    m: int,
    q: int,
    query1: list[int],
    query2: list[int],
    query3: list[int],
) -> list[int]:
    # TODO: Implement this function
    if step == 1:
        ret = do_step1(step, n, m, q, query1, query2, query3)
    if step == 2:
        ret = do_step2(step, n, m, q, query1, query2, query3)
    if step == 3:
        ret = do_step3(step, n, m, q, query1, query2, query3)
    if step == 4:
        ret = do_step3(step, n, m, q, query1, query2, query3)
    return ret
