#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

int apply_function(int A, int B, int x) { return A * x + B; }

int max_value(int N, int K, const vector<int> &A, const vector<int> &B) {
  int max_result = numeric_limits<int>::min();
  vector<int> indices(N);
  for (int i = 0; i < N; ++i) {
    indices[i] = i;
  }

  vector<int> comb(K);

  // 組み合わせを生成する
  auto combination = [&](auto &&self, int n, int k, int start, int depth) {
    if (depth == k) {
      // 順列を生成して評価する
      do {
        int x = 1;
        for (int i = 0; i < K; ++i) {
          x = apply_function(A[comb[i]], B[comb[i]], x);
        }
        max_result = max(max_result, x);
      } while (next_permutation(comb.begin(), comb.end()));
      return;
    }
    for (int i = start; i < n; ++i) {
      comb[depth] = indices[i];
      self(self, n, k, i + 1, depth + 1);
    }
  };

  // K個の関数の全ての組み合わせを試す
  combination(combination, N, K, 0, 0);

  return max_result;
}

int main() {
  int N, K;
  cin >> N >> K;
  vector<int> A(N), B(N);
  for (int i = 0; i < N; ++i) {
    cin >> A[i] >> B[i];
  }

  cout << max_value(N, K, A, B) << endl;

  return 0;
}
