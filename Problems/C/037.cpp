#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
#define rep(i, n) for(int i = 0; i < (n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  rep(i, n) {
    cin >> v[i];
  }

  ll ans = 0;
  ll tmp = 0;
  for(int i = 0; i < k - 1; i++) {
    tmp += v[i];
  }

  for(int i = 0; i < n - k + 1; i++) {
    tmp += v[i + k - 1];
    ans += tmp;
    tmp -= v[i];
  }
  cout << ans << endl;
  return 0;
}
