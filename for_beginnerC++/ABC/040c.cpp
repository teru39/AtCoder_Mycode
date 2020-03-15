#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  rep(i, n) {
    cin >> v[i];
  }
  vector<int> dp(100005);
  dp[0] = 0;
  dp[1] = abs(v[1] - v[0]);
  for(int i = 2; i < n; i++) {
    dp[i] =
        min(dp[i - 1] + abs(v[i] - v[i - 1]), dp[i - 2] + abs(v[i] - v[i - 2]));
  }
  cout << dp[n-1] << endl;
}
