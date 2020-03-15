#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, m;
  cin >> n >> m;
  if(n >= m) {
    cout << 0 << endl;
    return 0;
  }
  vector<int> v(m);
  rep(i, m) {
    cin >> v[i];
  }
  sort(all(v));
  vector<int> v_sub(m - 1);
  rep(i, m - 1) {
    v_sub[i] = abs(v[i + 1] - v[i]);
  }
  sort(all(v_sub));
  reverse(all(v_sub));
  int ans = v[v.size() - 1] - v[0];
  rep(i, n - 1) {
    ans -= v_sub[i];
  }
  cout << ans << endl;
}
