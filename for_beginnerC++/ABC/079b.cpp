#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<ll> dp(n+1);
  dp[0] = 2;
  dp[1] = 1;

  for(int i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  cout << dp[n] << endl;
}
