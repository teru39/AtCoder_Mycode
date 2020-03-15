#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int
main()
{
  int h, n;
  int inf = 1001001001;
  cin >> h >> n;
  vector<int> dp(h + 5, inf);
  dp[0] = 0;
  rep(i, n)
  {
    int a, b;
    cin >> a >> b;
    rep(j, h + 1)
    {
      int nj = min(j + a, h);
      dp[nj] = min(dp[nj], dp[j] + b);
    }
  }

  cout << dp[h] << endl;
}
