#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
  int n, ans = 0;
  vector<int> vec;
  cin >> n;
  rep(i, n)
  {
    int c;
    cin >> c;
    vec.push_back(c);
  }
  int now = 1;
  while (1)
  {
    now = vec[now - 1];
    ans++;
    if (now == 2)
    {
      cout << ans << endl;
      return 0;
    }
    if (ans >= n)
    {
      cout << -1 << endl;
      return 0;
    }
  }
}
