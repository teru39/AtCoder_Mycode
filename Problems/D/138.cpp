#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
#define rep(i, n) for(int i = 0; i < (n); i++)
#define all(v) (v).begin(), (v).end()

vector<int> to[200005];
vector<int> ans;

void dfs(int v, int p = -1) {
  for(int u : to[v]) {
    if(u == p) continue; //親だったらスルー
    ans[u] += ans[v];
    dfs(u, v);
  }
}

int main() {
  int n, q;
  cin >> n >> q;
  // 双方向の辺作成
  rep(i, n - 1) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    to[a].push_back(b);
    to[b].push_back(a);
  }
  ans.resize(n);
  rep(i, q) {
    int p, x;
    cin >> p >> x;
    p--;
    ans[p] += x;
  }
  dfs(0);

  rep(i, n) {
    cout << ans[i] << endl;
  }
  return 0;
}
