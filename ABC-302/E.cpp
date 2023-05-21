#include "iostream"
#include "stack"
#include "vector"

using namespace std;

// Union-Find
struct UnionFind {
  vector<int> par;

  UnionFind() {}
  UnionFind(int n) : par(n, -1) {}
  void init(int n) { par.assign(n, -1); }

  int root(int x) {
    if (par[x] < 0)
      return x;
    else
      return par[x] = root(par[x]);
  }

  bool issame(int x, int y) { return root(x) == root(y); }

  bool merge(int x, int y) {
    x = root(x);
    y = root(y);
    if (x == y)
      return false;
    if (par[x] > par[y])
      swap(x, y); // merge technique
    par[x] += par[y];
    par[y] = x;
    return true;
  }

  int size(int x) { return -par[root(x)]; }
};

// RMQ
template <class Monoid> struct RMQ {
  Monoid INF;
  int SIZE_R;
  vector<pair<Monoid, int>> dat;

  RMQ() {}
  RMQ(int n, const Monoid &inf) : INF(inf) { init(n, inf); }
  void init(int n, const Monoid &inf) {
    INF = inf;
    SIZE_R = 1;
    while (SIZE_R < n)
      SIZE_R *= 2;
    dat.assign(SIZE_R * 2, pair<Monoid, int>(INF, -1));
  }

  /* set, a is 0-indexed */
  void set(int a, const Monoid &v) { dat[a + SIZE_R] = make_pair(v, a); }
  void build() {
    for (int k = SIZE_R - 1; k > 0; --k) {
      dat[k] = max(dat[k * 2], dat[k * 2 + 1]);
    }
  }

  /* update, a is 0-indexed */
  void update(int a, const Monoid &v) {
    int k = a + SIZE_R;
    dat[k] = make_pair(v, a);
    while (k >>= 1)
      dat[k] = max(dat[k * 2], dat[k * 2 + 1]);
  }

  /* get {min-value, min-index}, a and b are 0-indexed */
  pair<Monoid, int> get(int a, int b) {
    pair<Monoid, int> vleft = make_pair(INF, -1), vright = make_pair(INF, -1);
    for (int left = a + SIZE_R, right = b + SIZE_R; left < right;
         left >>= 1, right >>= 1) {
      if (left & 1)
        vleft = max(vleft, dat[left++]);
      if (right & 1)
        vright = max(dat[--right], vright);
    }
    return max(vleft, vright);
  }
  inline Monoid operator[](int a) { return dat[a + SIZE_R].first; }

  /* debug */
  void print() {
    for (int i = 0; i < SIZE_R; ++i) {
      Monoid val = (*this)[i];
      if (val != INF)
        cout << val;
      else
        cout << "INF";
      if (i != SIZE_R - 1)
        cout << ",";
    }
    cout << endl;
  }
};
int main() {
  int n, q;
  cin >> n >> q;

  for (int i = 0; i < n; i++) {
    int l;
    cin >> l;
    if (l == 1) {
      int u, v;
      cin >> u >> v;
    } else {
      int u;
      cin >> u;
    }
  }
}
