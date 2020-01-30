#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
  int n, m, ans = 0;
  map<string, int> mp;
  cin >> n;
  rep(i, n)
  {
    string s;
    cin >> s;
    mp[s]++;
  }
  cin >> m;
  rep(i, m)
  {
    string s;
    cin >> s;
    mp[s]--;
  }
  for (auto x : mp)
  {
    ans = max(ans, x.second);
  }
  cout << ans << endl;
}
