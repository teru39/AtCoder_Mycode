#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int h, n;
  cin >> h >> n;
  int inf = 1001001001;
  vector<vector<int>> dp(n + 5, vector<int>(h + 1, inf));
  dp[0][0] = 0;
  rep(i, n) {
    int a, b;
    cin >> a >> b;
    for(int j = 0; j <= h; j++) {
      int nj = max(j - a, 0);
      dp[i + 1][j] = min(dp[i][j], dp[i + 1][nj] + b);
    }
  }
  cout << dp[n][h] << endl;
}
