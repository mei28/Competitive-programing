#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

pair<int, vector<int>> search_first_half(int mask, int N, int K,
                                         vector<vector<int>> &plans) {
  int cost = 0;
  vector<int> params(K, 0);
  for (int i = 0; i < N / 2; ++i) {
    if (mask & (1 << i)) {
      cost += plans[i][0];
      for (int j = 0; j < K; ++j) {
        params[j] += plans[i][j + 1];
      }
    }
  }
  return {cost, params};
}

pair<int, vector<int>> search_second_half(int mask, int N, int K,
                                          vector<vector<int>> &plans) {
  int cost = 0;
  vector<int> params(K, 0);
  for (int i = N / 2; i < N; ++i) {
    if (mask & (1 << (i - N / 2))) {
      cost += plans[i][0];
      for (int j = 0; j < K; ++j) {
        params[j] += plans[i][j + 1];
      }
    }
  }
  return {cost, params};
}

int main() {
  int N, K, P;
  cin >> N >> K >> P;
  vector<vector<int>> plans(N, vector<int>(K + 1));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < K + 1; ++j) {
      cin >> plans[i][j];
    }
  }

  unordered_map<vector<int>, int> first_half;
  for (int mask = 0; mask < (1 << (N / 2)); ++mask) {
    auto [cost, params] = search_first_half(mask, N, K, plans);
    if (first_half.count(params)) {
      first_half[params] = min(first_half[params], cost);
    } else {
      first_half[params] = cost;
    }
  }

  vector<pair<vector<int>, int>> sorted_first_half(first_half.begin(),
                                                   first_half.end());
  sort(sorted_first_half.begin(), sorted_first_half.end(),
       [](const auto &a, const auto &b) { return a.second < b.second; });

  int ans = INT_MAX;
  for (int mask = 0; mask < (1 << (N - N / 2)); ++mask) {
    auto [cost, params] = search_second_half(mask, N, K, plans);
    vector<int> needed(K);
    for (int i = 0; i < K; ++i) {
      needed[i] = P - params[i];
    }
    for (const auto &[key, value] : sorted_first_half) {
      bool ok = true;
      for (int i = 0; i < K; ++i) {
        if (key[i] < needed[i]) {
          ok = false;
          break;
        }
      }
      if (ok) {
        ans = min(ans, cost + value);
        break;
      }
    }
  }

  if (ans == INT_MAX) {
    cout << -1 << endl;
  } else {
    cout << ans << endl;
  }

  return 0;
}
