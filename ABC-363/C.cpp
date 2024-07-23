#include <bits/stdc++.h>
using namespace std;

// 文字列が回文かどうかをチェックする関数
bool isPalindrome(const string &s) {
  int n = s.size();
  for (int i = 0; i < n / 2; ++i) {
    if (s[i] != s[n - i - 1]) {
      return false;
    }
  }
  return true;
}

// 条件を満たす順列の数をカウントする関数
int countValidPermutations(int n, int k, const string &S) {
  set<string> perms;
  string sorted_S = S;
  sort(sorted_S.begin(), sorted_S.end());

  do {
    perms.insert(sorted_S);
  } while (next_permutation(sorted_S.begin(), sorted_S.end()));

  int valid_count = 0;

  for (const string &perm : perms) {
    bool contains_palindrome = false;

    for (int i = 0; i <= n - k; ++i) {
      if (isPalindrome(perm.substr(i, k))) {
        contains_palindrome = true;
        break;
      }
    }

    if (!contains_palindrome) {
      valid_count += 1;
    }
  }

  return valid_count;
}

int main() {
  int n, k;
  cin >> n >> k;
  string S;
  cin >> S;

  cout << countValidPermutations(n, k, S) << endl;

  return 0;
}
