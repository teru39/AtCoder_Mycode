#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, m;
  cin >> n >> m;
  vector<pair<ll, ll>> v(n);
  rep(i, n) {
    ll a, b;
    cin >> a >> b;
    v[i] = make_pair(a, b);
  }
  sort(all(v));
  ll ans = 0;
  rep(i, n) {
    ll a, b;
    tie(a, b) = v[i];
    if(b <= m) {
      m -= b;
      ans += a * b;
    } else {
      ans += a * m;
      break;
    }
  }

  cout << ans << endl;
}
