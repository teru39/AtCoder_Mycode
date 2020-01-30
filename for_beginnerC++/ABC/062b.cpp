#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main()
{
  int h, w;
  cin >> h >> w;
  rep(i, w + 2)
  {
    cout << '#';
  }
  cout << endl;
  rep(i, h)
  {
    string s;
    cin >> s;
    cout << '#' << s << '#' << endl;
  }
  rep(i, w + 2)
  {
    cout << '#';
  }

  cout << endl;
}
