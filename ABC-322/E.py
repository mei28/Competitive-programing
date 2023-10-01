def solve(N, K, P, development_plans):
    min_cost = float('inf')
    achieved = False
    
    # 組み合わせの中で、指定されたインデックス以降の開発案を使用して目標を達成できるか確認する
    def search(idx, current_params, current_cost):
        nonlocal min_cost, achieved
        
        # すべての開発案を試し終わったら、結果を確認する
        if idx == N:
            if all(x >= P for x in current_params):
                achieved = True
                min_cost = min(min_cost, current_cost)
            return
        
        # この開発案を使用する場合
        next_params = [current_params[j] + development_plans[idx][j+1] for j in range(K)]
        search(idx+1, next_params, current_cost + development_plans[idx][0])
        
        # この開発案を使用しない場合
        search(idx+1, current_params, current_cost)
    
    # 最初の開発案から検索を開始する
    search(0, [0]*K, 0)
    
    return min_cost if achieved else -1

# 入力部
N, K, P = map(int, input().split())
development_plans = [list(map(int, input().split())) for _ in range(N)]

# 出力部
print(solve(N, K, P, development_plans))

