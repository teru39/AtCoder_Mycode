#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 未完成
int main()
{
  int h, w;
  cin >> h >> w;
  rep(i, h)
  {
    string s;
    cin >> s;
    rep(j, w)
    {
      if (s[j] == '.')
        cout << 1 << endl;
      else
        cout << 2 << endl;
    }
  }
}
